
# SENTINEL EYE 

**Sentinel Eye** is a real-time face tracking system using Python, OpenCV, and Arduino. It detects faces using MediaPipe and controls two servo motors (pan/tilt) through an Arduino Uno to track the target.


## Hardware Setup

- Servo X → Arduino Pin 9  
- Servo Y → Arduino Pin 10  
- Connect both servos to 5V and GND

![System Diagram](https://media-hosting.imagekit.io/98b8ae1a6ae04808/Capture.PNG?Expires=1839000681&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=Mi~DtI3kkv9vaaLg-kzvnQUGPbnkJwWY1XufwLL5VeC6PMiVHFmizHrGuILvvZFvsKykvK2XU5hRqXGQtO26n4Rzi8yigILLHIr~ih5-KofLezaRNruJXtYNvzIBzyAjrwHbQJYKmiiq5g3BaK~gIH8od4vcoR0pZM3~ewa4-Dm25REg20LoU~3tDgmH9NcuIkyQDi8ol-re8vcKtt9Fp~m45k2znuhv1PdYuGeLQZpYpTXu-fITEzG4rqR6wZxWLevYf0Wa56zsVi0ugl3ZuXlWJ1vQTRWhWPK7ePc~VVB8DpxtbJkULNkXGLS1m8deJ99rr7QAYYcGcCsBgqfg-A__)
## Software Requirements

Install the following Python libraries:

```bash
  pip install opencv-python mediapipe pyfirmata numpy
```


## Running the Project

1' Upload StandardFirmata to Arduino via Arduino IDE.

2' Connect your webcam.

3' Run: `python sentinel_eye.py`
## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## 📁 Files

`sentinel_eye.py` – Main face-tracking script
`assets/wiring_diagram.png` – Wiring reference image


##  Notes

- Ensure your Arduino is connected to the correct COM port (default is `COM3` in the code).

- You can press q or click "CLOSE" to stop the program safely.
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Node, Express

