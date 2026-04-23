# OREO – ROS Based Quadruped Robot Dog


# OREO V2 – ROS Powered Vision-Based Quadruped Robot  
### Hack Club Advanced Robotics Project

OREO V2 is a next-generation quadruped robot dog powered by a Raspberry Pi 4 and Teensy microcontroller, upgraded from the original ESP32 version into a full ROS-based intelligent robotic platform.

This version adds:

- 🧠 Computer Vision
- 🐾 12 High-Torque (20kg) Servos
- 🤖 ROS 2 Architecture
- 📡 Behavior-Based Control System
- ❤️ Touch Interaction
- 📷 Person Detection & Following

OREO V2 is no longer just a walking robot — it is an intelligent robotic companion platform built under a constrained $395 budget.

---

# 📌 Project Overview

| Item | Description |
|------|-------------|
| Robot Type | Quadruped (4-legged) |
| Architecture | ROS 2 Modular System |
| Main Computer | Raspberry Pi 4 Model B (4GB) |
| Motor Controller | Teensy Microcontroller |
| Servos per Leg | 3 (Hip, Upper, Knee) |
| Total Servos | 12 × 20kg High Torque |
| Sensors | IMU + Touch Sensor + Camera |
| Frame | 3D Printed Spot Micro Style |
| Power | 2S/3S Li-ion / LiPo Battery |
| Budget | ~$395 USD |
| Difficulty | Intermediate → Advanced |

---

# 🎯 Vision & Purpose

OREO V2 was built to:

- Transition from beginner robotics to ROS-based research structure
- Integrate computer vision into a quadruped platform
- Maintain affordability under strict budget constraints
- Build a modular robotic system expandable to SLAM and AI
- Learn real robotics engineering workflow

This robot is designed as a stepping stone toward advanced robotic systems.

---

# 🧠 System Architecture

OREO V2 uses a layered robotics architecture.

## 🔵 High-Level Control (Raspberry Pi 4)

Runs:

- Ubuntu 22.04 (64-bit)
- ROS 2 Humble
- OpenCV
- Behavior Node
- Gait Controller Node
- Vision Node

Responsibilities:

- Computer vision
- State machine decisions
- Gait generation
- Touch reaction logic
- Serial communication with Teensy

---

## 🟢 Low-Level Control (Teensy)

Responsibilities:

- Servo PWM generation via PCA9685
- Reading IMU data
- Executing joint commands
- Sending feedback (IMU + joint states)

Communication via USB Serial to Raspberry Pi.

---

# 🤖 ROS Node Structure

## 1️⃣ teensy_interface_node
- Converts ROS messages to serial packets
- Publishes:
  - `/joint_states`
  - `/imu`
- Subscribes:
  - `/joint_targets`

---

## 2️⃣ gait_controller_node
- Generates walking/trot gait
- Uses IMU feedback for balance correction
- Publishes `/joint_targets`

---

## 3️⃣ vision_node
- Captures camera feed
- Runs OpenCV person detection
- Publishes:
  - `/person_detected`
  - `/target_direction`

---

## 4️⃣ behavior_node (Robot Brain)

Handles states:

- IDLE
- SEARCH
- FOLLOW
- SIT
- HAPPY
- LOW_BATTERY

Input:
- Vision topic
- Touch topic
- Battery monitoring

Output:
- `/cmd_gait`
- Emotion state commands

---

## 5️⃣ touch_node
Reads capacitive or pressure sensor  
Publishes `/touch_event`  

When touched → Robot enters HAPPY state.

---

# ✨ Features

- 🐕 Full 12 DOF quadruped
- ⚙️ 20kg high torque servos
- 📷 Real-time person detection
- 🚶 Follow-human functionality
- ❤️ Touch-based interaction
- 📐 IMU-based balance correction
- 🔋 Dedicated high-current servo rail
- 🧩 Modular ROS architecture
- 🔌 Teensy real-time motor control
- 🧠 AI-expandable platform

---

# 🧩 Mechanical Design

Based on improved Spot Micro style frame.

## Body
- Central frame housing electronics
- Battery compartment protected
- Ventilation for Raspberry Pi
- Camera mount on head

## Legs
- 3 DOF per leg
- Parallel linkage for better weight distribution
- Reinforced servo mounts for 20kg servos
- Proper torque alignment to reduce mechanical stress

---

# 🔋 Power System

- 2S or 3S Li-ion pack
- High-current BEC or buck converter for servos (6V recommended)
- Separate regulated 5V rail for Raspberry Pi

⚠ Always:
- Measure voltage before connecting servos
- Test load voltage drop
- Never power servos directly from Raspberry Pi

---

# 🛠 Assembly Workflow

## Step 1 – 3D Print Parts
- Body frame
- Leg assemblies (×4)
- Head mount
- Internal mounting brackets

## Step 2 – Mount Servos
- Center all 12 servos before installation
- Attach horns at neutral 90°
- Secure using metal gears and lock screws

## Step 3 – Install Electronics
- Mount Raspberry Pi
- Mount Teensy
- Connect PCA9685
- Connect IMU
- Install touch sensor on head/body

## Step 4 – Wiring
- Servo power rail separated
- Signal wires routed cleanly
- Verify ground common between Teensy & Pi

## Step 5 – Software Setup
- Install Ubuntu on Pi
- Install ROS 2
- Clone project repository
- Build workspace using colcon
- Flash Teensy firmware
- Connect via USB

## Step 6 – Calibration
- Zero joint angles
- Adjust trim offsets
- Test single leg motion
- Test gait without load
- Then test full body

---

# 📦 Bill of Materials (Approx Budget)

| Component | Qty |
|-----------|-----|
| Raspberry Pi 4 (4GB) | 1 |
| Teensy Microcontroller | 1 |
| PCA9685 Servo Driver | 1 |
| 20kg Metal Gear Servos | 12 |
| IMU Sensor | 1 |
| Camera Module | 1 |
| Touch Sensor | 1 |
| Battery Pack | 1 |
| Buck Converter | 1 |
| 3D Printed Parts | 1 Set |
| Screws & Inserts | Set |

Total Estimated Cost: ~$390–395 USD

---

# 🚀 Software Capabilities

Current:

- Basic walk
- Trot gait
- Person detection
- Follow mode
- Touch reaction mode

Future Upgrades:

- SLAM
- Obstacle detection
- AI voice recognition
- Depth camera integration
- Web dashboard control

---

# 🏁 What Makes OREO V2 Special

- Built under strict budget
- Uses ROS (research-level framework)
- Integrates vision and behavior logic
- Maintains affordable hardware
- Fully modular and expandable
- Combines mechanical + electrical + software engineering

OREO V2 is not just a robot dog.

It is a robotics learning platform engineered for serious development while staying budget-conscious.

---



---



[![Hack Club](https://assets.hackclub.com/flag-orpheus-top.svg)](https://hackclub.com/)
