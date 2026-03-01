# 🦾 OREO V2 Assembly & Configuration Guide

This document provides the step-by-step instructions for the physical assembly and wiring of the OREO V2 Quadruped using the Raspberry Pi 4 and Teensy 4.0 breakout system.

---

## 🛠 1. Hardware Assembly

### **Phase A: Mechanical Build**
1. **Servo Centering:** Connect your **Teensy 4.0** to the **PCA9685**. Power the PCA9685 with your 6V buck converter. Run a "Center" script to move all 12 servos to exactly 90°.
2. **Leg Construction:** * Attach the **Tibia** (lower leg) to the **Femur** (upper leg).
   * Attach the Femur to the **Coxa** (hip/shoulder).
   * Ensure the leg is at a right angle (90°) when the servo is at its center position.
3. **Chassis:** Mount the **Raspberry Pi 4** and **Teensy 4.0** on the main body. Use standoffs to ensure the boards don't touch the plastic directly to allow for airflow.

---

## 🔌 2. Wiring Logic (The Breakout System)

Since we are using standard breakout boards, follow this wiring map exactly:

### **Power Distribution**
* **Battery (2S/3S Li-ion)** -> **XT60 Connector**.
* **XT60** -> Splits to **Two Buck Converters**:
    1. **Buck 1 (6V 10A):** Connects to the **Screw Terminals** on the PCA9685 (Powers the 12 Servos).
    2. **Buck 2 (5V 3A):** Connects to the **USB-C port** of the Raspberry Pi 4.
* **Teensy 4.0:** Powered via the **USB Cable** connected to the Raspberry Pi 4.

### **Data Connections**
| Component | Pin on Teensy 4.0 | Pin on Module |
| :--- | :--- | :--- |
| **PCA9685** | Pin 18 (SDA) | SDA |
| **PCA9685** | Pin 19 (SCL) | SCL |
| **MPU6050** | Pin 18 (SDA) | SDA |
| **MPU6050** | Pin 19 (SCL) | SCL |
| **MPU6050** | GND / 3.3V | GND / 3.3V |

---

## 📂 3. ROS 2 Humble Project Structure

On your Raspberry Pi 4 (Ubuntu 22.04), your workspace should be organized as follows:

```text
oreo_ws/
└── src/
    └── oreo_robot/
        ├── package.xml
        ├── setup.py
        ├── oreo_robot/
        │   ├── __init__.py
        │   ├── gait_controller.py   # Walking logic/IK
        │   ├── serial_bridge.py      # Communication with Teensy
        │   └── vision_node.py        # Pi Camera tracking
        └── launch/
            └── robot.launch.py       # Starts all nodes at once
