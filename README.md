# Gesture-Controlled Gaming Glove

This project presents a **gesture-controlled glove** for gaming applications using an **Arduino Uno** and an **MPU6050** motion sensor. By capturing hand movements and translating them into keyboard commands, the glove offers an **immersive and hands-free** gaming experience.

---

## Project Overview

The glove leverages the **MPU6050** IMU (3-axis accelerometer + 3-axis gyroscope) to detect hand gestures such as **tilting left/right** and **moving up/down**. These gestures are processed by an **Arduino Uno**, and corresponding keyboard inputs (arrow keys) are simulated using Python on a connected PC.

### Key Features
- Intuitive gesture-based control for games
- Real-time gesture-to-keypress mapping
- HID interface via Python (`pyautogui`, `pyserial`, `keyboard`)
- Wearable and low-cost DIY solution

---



## System Architecture

1. **MPU6050 Sensor**: Captures hand acceleration and gyroscopic data.
2. **Arduino Uno**: Reads sensor data via I2C and transmits gestures via serial.
3. **Python Script**:
   - `pyserial`: Receives data from Arduino.
   - `pyautogui` / `keyboard`: Simulates arrow keypresses.
4. **Glove Integration**: Hardware is embedded into a glove for natural control.

---

## Results

- **Low-latency** real-time control
- **High accuracy** in gesture detection for moderate hand movements
-  Tested on simple games with responsive arrow key simulation

> **Note**: Minor inaccuracies were observed during very rapid hand movements, suggesting room for signal filtering improvements.

---

## Requirements

### Hardware
- Arduino Uno
- MPU6050 Sensor
- Glove (for mounting)
- Jumper wires
- USB Cable

### Software
- Arduino IDE
- Python 3.x
- Python Libraries:
  - `pyserial`
  - `pyautogui`
  - `keyboard`

Install dependencies:
```bash
pip install pyserial pyautogui keyboard
