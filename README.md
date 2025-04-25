
<br>

<div id="top">
<p align="center">
  <a href="https://github.com/sarunk-dev/SentineL-Eye" target="_blank" rel="noopener noreferrer">
    <img width = "200" src="https://i.postimg.cc/MHBg5XZC/1-initial-letter-e-for-eye-vision-logo-design-vector.jpg">
  </a>
</p>
</div>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/ssrikanthreddy/Alertr.svg)](https://github.com/sarunk-dev/SentineL-Eye/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/ssrikanthreddy/Resonex)](https://github.com/sarunk-dev/SentineL-Eye/pulls)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE.md)

**Sentinel Eye** is a real-time face tracking system using Python, OpenCV, and Arduino. It detects faces using MediaPipe and controls two servo motors (pan/tilt) through an Arduino Uno to track the target.

</div>

## 💫 Features

- **Real-Time Face Tracking:** Uses a webcam and Mediapipe's face detection to follow a person's face dynamically.

- **Dual Servo Control:** Controls two servo motors (X and Y axis) via Arduino (Pin 9 and 10) for precise panning and tilting.

- **Target Selection UI:** Displays selectable buttons for choosing one target when multiple faces are detected.

- **Smooth Movement:** Implements interpolated and gradual servo positioning for stable and natural tracking.

- **Auto Recenter:** Repositions the servos to default center angles (90°) when no face is detected or upon exit.
## ⚒️ Built Using
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

## 🖥️ System Diagram
<div align="center">

![](https://media-hosting.imagekit.io/98b8ae1a6ae04808/Capture.PNG?Expires=1839000681&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=Mi~DtI3kkv9vaaLg-kzvnQUGPbnkJwWY1XufwLL5VeC6PMiVHFmizHrGuILvvZFvsKykvK2XU5hRqXGQtO26n4Rzi8yigILLHIr~ih5-KofLezaRNruJXtYNvzIBzyAjrwHbQJYKmiiq5g3BaK~gIH8od4vcoR0pZM3~ewa4-Dm25REg20LoU~3tDgmH9NcuIkyQDi8ol-re8vcKtt9Fp~m45k2znuhv1PdYuGeLQZpYpTXu-fITEzG4rqR6wZxWLevYf0Wa56zsVi0ugl3ZuXlWJ1vQTRWhWPK7ePc~VVB8DpxtbJkULNkXGLS1m8deJ99rr7QAYYcGcCsBgqfg-A__)

</div>

## 🏃 Running the Project

To run Sentinel eye locally, follow these steps:

*1 - Upload StandardFirmata to Arduino via Arduino IDE.*

  → *open Arduino IDE* `File → Examples → Firmata → StandardFirmata` *Select COM & Click Upload*
  
*2 - Connect your webcam.*

*3 - Create a virtual environment in VS code `python -m venv venv`*

*4 - Activate the virtual environment `.\venv\Scripts\activate`*

*5 - Run the python file.*

```bash
  python sentinel_eye.py
```
<div align="center">
  
![](<https://media-hosting.imagekit.io/febff6da324140b2/ezgif-7cc6609cca1031.gif?Expires=1840206310&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=EPOVPnkRMNXCXmTgnMAspiimbu4PNe9qzB3Dfbx8h0KQYKYfOKIs0Rgicr75x9See40ieD4XWxHJONgLvjsd5av2HvAu1aOcTrLGrdQoM2fDezi7wFLX0uy6qxGAuQvRI2CEE8sY7mFv4LoZRxqoQeCNjYY7D1dlFDXWugoP-Yywyc7dsCsH-kZnGR6BBGsJ9GmC3I4y1w54xkb1TQe8r8uDewINT79bdiFvdu7dit1OqvgQFZDL3vlfRlsswcO5j6sN137i7PZ2wEUe5wU07iFS-AjONK3f6Q5hyG4tFIaNz9c6rAGAlybe5qfvHbJiAum1ML8bnpWRPDK1Q-YqrA__>)


</div>



  
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


<div align="center">
  
![Image](https://github.com/user-attachments/assets/9db9361f-f533-40e3-af89-cc5af37dcb2e)

</div>

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

