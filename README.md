# 🐕 OREO – ESP32 Based Quadruped Robot Dog

<a href="https://hackclub.com/"><img style="position: absolute; top: 0; left: 10px; border: 0; width: 256px; z-index: 999;" src="https://assets.hackclub.com/banners/2026.svg" alt="Hack Club"/></a>

OREO is a compact, lightweight, and beginner-friendly **3D-printed quadruped robot dog** powered by an **ESP32** and servo motors.  
The project is designed to teach **quadruped robotics, PCB design, and mechanical joints** in a simple, hands-on way.

Unlike many complex robot dogs that use 3 servos per leg and heavy frames, OREO focuses on **simplicity without losing stability**.

---

## 📌 Project Overview

| Item | Description |
|----|----|
| Robot Type | Quadruped (4-legged) |
| Controller | ESP32 |
| Servos per Leg | 2 (Hip + Knee) |
| Total Servos | 8 |
| Structure | Fully 3D Printed |
| Power | Dual 18650 Li-ion |
| Difficulty | Beginner → Intermediate |
| Goal | Learning walking robot fundamentals |

---

## 🎯 Why I Built This

I wanted to build a robot dog that:
- Is **not over-complicated**
- Uses **fewer servos**
- Is **easy to assemble and repair**
- Still walks **smoothly and stably**

While building this project, I learned about:
- Quadruped leg movement
- Gait timing and stability
- Servo power management
- PCB design mistakes and fixes
- Mechanical stress in 3D printed joints

This project went through **multiple failed revisions** before reaching a working design.

---

## ✨ Features

- 🐾 4-leg quadruped robot
- ⚙️ Only **2 servos per leg**
- 🖨 Fully 3D printed body and joints
- 🧠 ESP32 based control system
- 🔌 Custom PCB for clean wiring
- 🔋 External DC-DC regulated servo power
- 🔧 Modular and easy-to-repair design

---

## 🧩 Mechanical Design

### Body
- Single main body print
- Bottom opening for PCB and battery
- Printed lid secured with screws
- Clean internal space for wiring

### Leg Design
- Initial version used **3 servos per leg**
- Redesigned to **2 servos per leg**
- Reduced cost, weight, and software complexity
- Uses tendon support for stability

---

## 🖨 3D Printing Instructions

### Printing Orientation
- Rotate the **body upside down** before slicing
- Large opening must face upward

### Support Requirements
| Part | Supports |
|---|---|
| Body | Yes |
| Lid | No |
| Hip / Ham | No |
| Shank | No |

### Important Notes
- Print **Hip and Ham parts twice** (Left + Right)
- Drill shank joint using **3mm drill bit**
- Use **screws instead of filament pins**
- Tendons are made from **straightened paper clips**

---

## 🔌 PCB & Electronics

### Custom PCB
The PCB was designed to:
- Reduce wire clutter
- Improve reliability
- Add a strong **USB Type-B port**

### Power System
- Dual 18650 batteries (~7.4V)
- DC-DC buck/boost converter
- Servo voltage set to **exactly 5V**

> ⚠️ Always adjust the DC-DC output before connecting servos to prevent damage.

The PCB is mounted inside the body using **four M2 screws**.

---

## 🧠 Software / Firmware

### Firmware Features
- Servo mapping
- Inverse kinematics
- Leg timing control
- Basic walking gait

### Debug Issue Faced
- Hip and knee servos were initially swapped
- Robot movement was unstable
- Fixed by swapping pins in the config file
- Walking became smooth after correction

INA219 current sensor code exists but was removed in the final build for simplicity.

---

## 🛠 Assembly Guide

### Step 1 – Print Parts
- Body  
- Lid  
- Hip (L + R)  
- Ham (L + R)  
- Shank  
- Servo brackets  
- Tendon pins  

---

### Step 2 – Prepare Joints
- Insert **M3 and M2.5 threaded inserts**
- Assemble legs:
  - Hip → Ham (servo mounted)
  - Ham → Shank (M3 screw + lock nut)
- Create tendons using paper clips

---

### Step 3 – Mount Servos
- Total servos: **8**
- Upper servo = Hip
- Lower servo = Knee
- Center servo horns before tightening

---

### Step 4 – Electronics
- Mount ESP32 on PCB
- Connect servos to correct headers
- Connect battery and DC-DC converter
- Verify **5V output**

---

### Step 5 – Final Assembly
- Insert PCB and battery from bottom
- Arrange wiring neatly
- Close body with printed lid

---

### Step 6 – Upload Code
- Connect ESP32 via USB
- Upload firmware
- Adjust servo trim values

---

### Step 7 – Testing
- Test each leg individually
- Place robot on flat surface
- Run walking program
- Fine-tune servo angles for balance

---

## 📦 Bill of Materials (BOM)

| Component | Qty | Purpose |
|---|---|---|
| ESP32 Dev Board | 1 | Main controller |
| Servo Motors | 8 | Leg movement |
| 3D Printed Parts | 1 set | Structure |
| Dual 18650 Holder | 1 | Power |
| 18650 Batteries | 2 | Supply |
| DC-DC Converter | 1 | 5V servo power |
| M3 Screws | Set | Joints |
| M2 / M2.5 Screws | Set | PCB mounting |
| Threaded Inserts | Set | Strength |
| Dupont Wires | Few | Signals |
| Paper Clips | 4 | Tendons |
| Custom PCB (Optional) | 1 | Wiring cleanup |

---

## 🔄 PCB Version 2 Update

Improvements:
- All 3 servo positions available per leg
- Clean and consistent connector layout

Header mapping:
- **B headers** → Hip servos  
- **G headers** → Knee servos  
- **A headers** → Unused  

No software pin swapping required.

---

## 🏁 Conclusion

OREO was a challenging but rewarding project.  
Mistakes in PCB design, servo wiring, and mechanical strength became valuable learning experiences.

This robot proves that:
- Quadruped robots don’t need extreme complexity
- Simple designs can still walk reliably
- Beginners *can* build walking robots successfully

Perfect starting point for:
- Advanced gaits
- Sensors
- Vision
- AI-based control

---

[![Hack Club](https://assets.hackclub.com/flag-orpheus-top.svg)](https://hackclub.com/)
