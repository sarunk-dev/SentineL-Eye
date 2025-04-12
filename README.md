
# SENTINEL EYE 

**Sentinel Eye** is a real-time face tracking system using Python, OpenCV, and Arduino. It detects faces using MediaPipe and controls two servo motors (pan/tilt) through an Arduino Uno to track the target.

## 🌟 Overview

Sentinel Eye addresses the need for smart surveillance by proposing a real-time face tracking system using MediaPipe and Arduino-controlled servos. It enables accurate face detection, smooth pan-tilt tracking, and user-selectable targets, offering a low-cost, scalable solution for security and defense applications.
## 💫 Features

 **Real-Time Face Tracking:** Uses a webcam and Mediapipe's face detection to follow a person's face dynamically.

 **Dual Servo Control:** Controls two servo motors (X and Y axis) via Arduino (Pin 9 and 10) for precise panning and tilting.

 **Target Selection UI:** Displays selectable buttons for choosing one target when multiple faces are detected.

 **Smooth Movement:** Implements interpolated and gradual servo positioning for stable and natural tracking.

 **Auto Recenter:** Repositions the servos to default center angles (90°) when no face is detected or upon exit.
## ⚒️ Built Using
<h3 align="left">Connect with me:</h3>
<p align="left">
</p>

<h3 align="left"></h3>
<p align="left"> <a href="https://www.arduino.cc/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/arduino-1.svg" alt="arduino" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## 🚀 Getting Started
This guide will walk you through the steps to install and run the Sentinel EYE locally on your machine.
## ⚙️ Prerequisites

Before you begin, make sure you have the following software installed on your machine:

- Pyhton (version 3.12.4)
- Arduino IDE (Latest version)
## 📦 Installation
To install Sentinel eye, follow these steps

1 Clone the repository:
```bash
  https://github.com/sarunk-dev/SentineL-Eye.git
```
2 Navigate to the project directory
```bash
  cd sentinel_eye
```
3 Install the required Python libraries
```bash
pip install opencv-python mediapipe pyfirmata numpy
```
## 🔧 Hardware Setup

- Servo X → Arduino Pin 9  
- Servo Y → Arduino Pin 10  
- Connect both servos to 5V and GND
- USB Cable → Laptop
- Webcam → Video Input

![System Diagram](https://media-hosting.imagekit.io/98b8ae1a6ae04808/Capture.PNG?Expires=1839000681&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=Mi~DtI3kkv9vaaLg-kzvnQUGPbnkJwWY1XufwLL5VeC6PMiVHFmizHrGuILvvZFvsKykvK2XU5hRqXGQtO26n4Rzi8yigILLHIr~ih5-KofLezaRNruJXtYNvzIBzyAjrwHbQJYKmiiq5g3BaK~gIH8od4vcoR0pZM3~ewa4-Dm25REg20LoU~3tDgmH9NcuIkyQDi8ol-re8vcKtt9Fp~m45k2znuhv1PdYuGeLQZpYpTXu-fITEzG4rqR6wZxWLevYf0Wa56zsVi0ugl3ZuXlWJ1vQTRWhWPK7ePc~VVB8DpxtbJkULNkXGLS1m8deJ99rr7QAYYcGcCsBgqfg-A__)
## 🏃 Running the Project

To run Sentinel eye locally, follow these steps:

*1 - Upload StandardFirmata to Arduino via Arduino IDE.*

*2 - Connect your webcam.*

*3 - Create a virtual environment `python -m venv venv`*

*4 - Activate the virtual environment `.\venv\Scripts\activate`*

*5 - Run the python file.*

```bash
  python sentinel_eye.py
```


## 🛠 Issue Fix:

**Attribute Error:** module 'inspect' has no attribute 'getargspec'


*The `inspect.getargspec()` function was removed in **Python 3.11+**. 
This function is still used in `pyfirmata`.*

**Option 1:** Downgrade Python to 3.10 or Below 


**Option 2:** Patch pyfirmata
- Navigate to your `venv/Lib/site-packages/pyfirmata/ directory`

- Open `pyfirmata.py`

*Find this line (usually around line 185):*

```bash
  len_args = len(inspect.getargspec(func)[0])
```
*Replace it with:*
```bash
  len_args = len(inspect.getfullargspec(func).args)
```
*Save and re-run your script.*

## 🎯 Usage

-  **Surveillance & Monitoring:** Tracks human faces in real-time for security monitoring in homes, offices, or public spaces.

-  **Defense Applications:** Can be used at entry checkpoints to automatically follow individuals, aiding guards in observing behavior.

-  **Robotics Vision System:** Acts as a vision-based input system for autonomous robots to detect and follow humans.

-  **AI-Assisted Targeting Systems:** Basic prototype for AI-based object or face tracking in defense drones or turrets (lethal).
## 🤝 Contributing

We appreciate your interest in contributing to our project! Whether you want to report a bug, propose new features, or submit improvements to the existing codebase, your contributions are highly valued.
## 📞 Contact

For inquiries, please contact [seerlaarun.dev@gmail.com].
## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

