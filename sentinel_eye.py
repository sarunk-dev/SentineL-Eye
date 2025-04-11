import cv2
import mediapipe as mp
import pyfirmata
import numpy as np

# Setup camera
cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

# Setup Arduino
port = "COM3"
board = pyfirmata.Arduino(port)
servo_pinX = board.get_pin('d:9:s')
servo_pinY = board.get_pin('d:10:s')

servoPos = [90, 90]

# Mediapipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.7)

# Define button positions and sizes
close_button_pos = (ws - 180, hs - 50)
close_button_size = (110, 40)
close_program = False

selected_target = None
target_buttons = []
target_selected = False

def smooth_move(current_pos, target_pos, step=1):
    if current_pos < target_pos:
        return min(current_pos + step, target_pos)
    elif current_pos > target_pos:
        return max(current_pos - step, target_pos)
    return current_pos

def smooth_recenter():
    global servoPos
    while servoPos[0] != 90 or servoPos[1] != 90:
        servoPos[0] = smooth_move(servoPos[0], 90, step=1)
        servoPos[1] = smooth_move(servoPos[1], 90, step=1)
        servo_pinX.write(servoPos[0])
        servo_pinY.write(servoPos[1])
        cv2.waitKey(10)

def click_event(event, x, y, flags, param):
    global close_program, selected_target, target_selected
    if event == cv2.EVENT_LBUTTONDOWN:
        bx, by = close_button_pos
        bw, bh = close_button_size
        if bx <= x <= bx + bw and by <= y <= by + bh:
            close_program = True

        for i, (tx, ty, tw, th) in enumerate(target_buttons):
            if tx <= x <= tx + tw and ty <= y <= ty + th:
                selected_target = i
                target_selected = True
                break

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", click_event)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(img_rgb)

    target_buttons = []
    if results.detections:
        for i, detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            fx, fy = bbox[0] + bbox[2] // 2, bbox[1] + bbox[3] // 2
            pos = [fx, fy]

            if len(results.detections) > 1:
                button_pos = (10, hs - (len(target_buttons) + 1) * 50)
                button_size = (200, 40)
                target_buttons.append((button_pos[0], button_pos[1], button_size[0], button_size[1]))
                cv2.rectangle(img, button_pos, (button_pos[0] + button_size[0], button_pos[1] + button_size[1]), (0, 255, 0), -1)
                cv2.putText(img, f"Select Target {i+1}", (button_pos[0] + 5, button_pos[1] + 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

            if target_selected and i == selected_target or len(results.detections) == 1:
                servoX = np.interp(fx, [0, ws], [180, 0])
                servoY = np.interp(fy, [0, hs], [0, 180]) - 40
                servoX = np.clip(servoX, 0, 180)
                servoY = np.clip(servoY, 0, 180)

                servoPos[0] = servoX
                servoPos[1] = servoY

                cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)
                cv2.putText(img, str(pos), (fx + 15, fy - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                cv2.line(img, (0, fy), (ws, fy), (0, 0, 0), 2)
                cv2.line(img, (fx, hs), (fx, 0), (0, 0, 0), 2)
                cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)
                cv2.putText(img, "TARGET LOCKED", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    else:
        servoPos[0] = smooth_move(servoPos[0], 90, step=1)
        servoPos[1] = smooth_move(servoPos[1], 90, step=1)

        cv2.putText(img, "NO TARGET", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.circle(img, (640, 360), 80, (0, 0, 255), 2)
        cv2.circle(img, (640, 360), 15, (0, 0, 255), cv2.FILLED)
        cv2.line(img, (0, 360), (ws, 360), (0, 0, 0), 2)
        cv2.line(img, (640, hs), (640, 0), (0, 0, 0), 2)

    cv2.putText(img, f'Servo X: {int(servoPos[0])} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.putText(img, f'Servo Y: {int(servoPos[1])} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    servo_pinX.write(servoPos[0])
    servo_pinY.write(servoPos[1])

    bx, by = close_button_pos
    bw, bh = close_button_size
    cv2.rectangle(img, (bx, by), (bx + bw, by + bh), (0, 0, 255), -1)
    cv2.putText(img, "CLOSE", (bx + 10, by + 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if close_program:
        smooth_recenter()
        break

cap.release()
cv2.destroyAllWindows()
