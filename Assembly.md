# 🦾 OREO V2 Assembly & Development Guide

This document contains the hardware wiring instructions and the advanced AI prompt required to generate the full control software.

---

## 🛠 Part 1: ASSEMBLE.md (Wiring & Hardware)

### 1. Electronics Layout
Since we are using **breakout boards**, no custom PCB is required. All components connect via jumper wires and a central I2C bus.

| Component | Connection Type | Destination | Pins/Ports |
| :--- | :--- | :--- | :--- |
| **Teensy 4.0** | Data | Raspberry Pi 4 | USB-C to USB-A Cable |
| **Teensy 4.0** | I2C (Logic) | PCA9685 | Pin 18 (SDA) -> SDA / Pin 19 (SCL) -> SCL |
| **Teensy 4.0** | I2C (Logic) | MPU6050 | Pin 18 (SDA) -> SDA / Pin 19 (SCL) -> SCL |
| **PCA9685** | High Power | 6V 10A Buck | Blue Screw Terminals (V+ and GND) |
| **12x Servos** | PWM | PCA9685 | Channels 0-11 (Check Leg Mapping) |
| **RPi 4** | Power | 5V 3A Buck | USB-C Power Port or GPIO Pins 2/6 |

### 2. Leg Mapping (Standard 12-DOF)
Connect your servos to the PCA9685 in this order to match standard gait code:
* **Front Right (FR):** Hip = 0, Femur = 1, Tibia = 2
* **Front Left (FL):** Hip = 4, Femur = 5, Tibia = 6
* **Back Right (BR):** Hip = 8, Femur = 9, Tibia = 10
* **Back Left (BL):** Hip = 12, Femur = 13, Tibia = 14

### 3. Assembly Steps
1.  **Neutral Calibration:** Power your PCA9685 and use a simple "90-degree" sketch to center all 12 servos before attaching leg horns.
2.  **Mounting:** Secure the Raspberry Pi 4 and Teensy 4.0 to the main chassis using M3 screws.
3.  **Heat Management:** Attach the Cooling Fan to the Pi 4. The 20kg servos and buck converters will get hot during 10+ minutes of use; ensure the chassis has airflow.
4.  **IMU Placement:** Mount the MPU6050 as close to the **dead center** of the robot as possible for the best balance data.

---

## 🤖 Part 2: Antigravity AI Code Generation Prompt

*Copy the text below and paste it into an AI (like ChatGPT, Claude, or Antigravity) to generate your entire codebase.*

> **System Role:** You are an expert Robotics Engineer specializing in ROS 2 Humble and Teensy microcontrollers.
>
> **Project Goal:** Generate the software for "OREO V2," a 12-DOF quadruped robot.
>
> **Hardware Specs:**
> - Master: Raspberry Pi 4 (Ubuntu 22.04 + ROS 2 Humble).
> - Slave: Teensy 4.0 connected to Pi via USB Serial.
> - Actuators: 12x 20kg Servos via PCA9685 (I2C).
> - Sensor: MPU6050 (I2C) for balance.
>
> **Requirement 1: Teensy Firmware (C++)**
> - Create a sketch using `Adafruit_PWMServoDriver.h` and `Wire.h`.
> - Implement a serial parser that accepts a string like: `S,0,90,45,180...[12 angles]`.
> - Include a safety "Soft Start" to prevent the 20kg servos from jerking on power-up.
> - Send MPU6050 Pitch and Roll back to the Pi at 50Hz.
>
> **Requirement 2: ROS 2 Humble Python Node (Gait Engine)**
> - Create a node called `oreo_gait_engine`.
> - Implement Inverse Kinematics (IK) for a 3-segment leg (Coxa, Femur, Tibia).
> - Create a "Trot Gait" trajectory generator.
> - Subscribe to `/cmd_vel` (geometry_msgs/msg/Twist) to control speed and direction.
> - Publish the 12 target angles to the Teensy via `pyserial`.
>
> **Requirement 3: ROS 2 Vision Node**
> - Create a node using `opencv` and `cv_bridge` to process the RPi Camera feed.
> - Implement simple color-based or face tracking that outputs a `/cmd_vel` message to make the robot follow a target.
>
> **Output Format:** Provide the Teensy `.ino` file first, followed by the ROS 2 Python nodes and a `setup.py` file.

---

## 📦 Part 4: Final Project Structure for GitHub
Ensure your repository looks like this:
```text
OREO_V2/
├── hardware/
│   ├── wiring_diagram.png
│   └── bom.csv
├── firmware/
│   └── oreo_teensy_control.ino
└── ros2_ws/
    └── src/
        └── oreo_robot/
            ├── oreo_robot/
            │   ├── gait_engine.py
            │   ├── serial_bridge.py
            │   └── vision_node.py
            ├── launch/
            │   └── robot.launch.py
            └── package.xml
