# 🖐️ AI Virtual Mouse Using Hand Gestures

An AI-based virtual mouse system that allows users to control the mouse cursor using hand gestures captured through a webcam.  
This project removes the need for a physical mouse by using real-time computer vision and hand landmark detection.

---

## 🚀 Features
- Smooth cursor movement
- Left click using **thumb + index finger**
- Right click using **index + middle finger**
- Scroll using **two fingers**
- Pause / Resume control using **fist gesture**
- Real-time hand tracking
- No external hardware required

---

## 🛠️ Tech Stack
- **Python**
- **OpenCV**
- **MediaPipe**
- **PyAutoGUI**

---

## 🧠 How It Works
- The webcam captures live video frames.
- MediaPipe detects 21 hand landmarks in real time.
- Finger positions are mapped to screen coordinates.
- Gestures are interpreted to perform mouse actions such as click, scroll, and pause.
- PyAutoGUI controls the system mouse based on detected gestures.

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/AI-Virtual-Mouse-Using-Hand-Gestures.git
cd AI-Virtual-Mouse-Using-Hand-Gestures

python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install mediapipe==0.10.9 opencv-python pyautogui
▶️ How to Run
bash
Copy code
python hand.py
