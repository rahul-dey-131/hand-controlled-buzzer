## ✋🎵 Hand-Gesture Controlled Buzzer using MediaPipe & Arduino

This is a fun little project that uses **hand tracking** with a webcam to control a **buzzer’s pitch** on an Arduino — just by changing the distance between your **thumb and index finger**!

It’s like playing a virtual theremin... but with your fingers ✨

---

### 🚀 What It Does

* Detects your hand using **MediaPipe** (via Python & OpenCV).
* Calculates the **distance** between your **thumb** and **index fingertip**.
* Sends that distance value to **Arduino over Serial**.
* The Arduino:

  * **Maps the distance** to a **sound frequency**.
  * Plays a tone using a **passive buzzer**.
  * Turns on an **LED** while buzzing.

You move your fingers — the pitch changes 🎶
Move too close or too far — the buzzer stops 🔇

---

### 🛠️ Tools & Tech

* **Python** (OpenCV, MediaPipe)
* **Arduino UNO**
* **Passive Buzzer**
* **LED (optional but recommended)**
* **Serial Communication**

---

### 🖼️ How It Works

1. **Python Side**:

   * Uses `mediapipe` to track hand landmarks.
   * Measures the real-time distance between two fingertips.
   * Sends that value over Serial (`COM3`).

2. **Arduino Side**:

   * Reads the value.
   * Maps it to a frequency range (e.g., 20–2000 Hz).
   * Generates a tone using PWM logic.
   * Lights up pin 13 when buzzing.

---

### 🎥 Demo

*(Add a short demo video or GIF if possible showing the finger movement and sound effect)*

---

### 📁 Files in This Repo

* `handTrackingModule.py`: Custom module for hand detection using MediaPipe.
* `buzzFreqHandControl.py`: Main Python script for camera input and Serial communication.
* `HandControlledFrequency.ino`: Arduino sketch to generate a tone based on finger distance.

---

### 🧠 Learning Goals

* Basics of **Computer Vision & Gesture Tracking**
* Using **MediaPipe Hands** for real-time landmark detection
* Mapping values to physical outputs using **Arduino**
* Smooth **Serial communication** between Python and Arduino

---

### 🔌 Setup Instructions

1. **Hardware**:

   * Connect buzzer to pin 7 and GND
   * Connect LED to pin 13 (optional)
   * Upload `HandControlledFrequency.ino` to your Arduino

2. **Python**:

   ```bash
   pip install opencv-python mediapipe pyserial
   ```

3. **Run the script**:

   ```bash
   python buzzFreqHandControl.py
   ```

---

### 🤓 Credits & Inspiration

This project is inspired by gesture-based control systems and a passion for blending **physical computing** with **computer vision**. It was a learning experiment — and honestly, just a lot of fun!

---
