	
<a href="https://hackclub.com/"><img style="position: absolute; top: 0; left: 10px; border: 0; width: 256px; z-index: 999;" src="https://assets.hackclub.com/flag-orpheus-top.svg" alt="Hack Club"/></a>

🐕 OREO – Robot Dog

Oreo is a small 3D printed robot dog made using ESP32 and servo motors. It is designed to be compact, lightweight and easy to assemble. The body has clean internal space for battery and PCB so wiring does not become messy. The robot uses a simple two-servo per leg mechanism which gives decent and stable walking.

This robot is mainly built for learning quadruped robotics, PCB design and mechanical joints in a beginner friendly way.

Why I Built This

I wanted to build a robot dog that is not too complex but still functional. Many quadruped robots online use 3 servos per leg and complicated frames. I tried to simplify the design and reduce the servo count while keeping good stability.

While building this project I learned a lot about:

Quadruped leg movement

Servo power management

PCB mistakes and fixing them

Mechanical strength of 3D printed joints

This project went through multiple revisions and mistakes before finally working properly.

Project Features

4 leg quadruped robot

Only 2 servos per leg (hip + knee)

Fully 3D printed structure

ESP32 based control

Custom PCB with external USB port

Modular and easy to repair design

Design & Hardware

The body is mostly printed as one main frame with a bottom opening. This opening is used for battery and PCB access. A printed lid is used to close the body.

Originally the leg used 3 servos (Alpha, Beta, Gamma). Later I redesigned the structure so only hip and knee servos are needed. This reduced cost and complexity.

3D Printing Details
Printing Notes

Rotate the body upside down before slicing so the large opening faces upward

Use supports only for the body

Lid does not need supports

Hip and ham parts must be printed twice (left and right)

Drill the shank joint hole using 3mm drill bit

Tendons are made using straightened paper clips

All joints use screws instead of filament pins so the joints last longer.

PCB & Electronics

I designed a custom PCB mainly to clean up wiring. I also added a full size USB Type-B connector because the ESP32 micro USB port is small and easy to break.

A DC-DC buck/boost converter is used to power all servos. Before soldering, I adjusted the output voltage to exactly 5V to avoid servo damage.

The PCB is mounted inside the body using four M2 screws.

Software / Firmware

I use custom firmware for:

Servo mapping

Leg inverse kinematics

Timing and movement control

Basic walking gait

At first I connected wrong servo positions on the PCB. Because of this the robot was moving incorrectly. I fixed this by swapping hip and knee pins in the config file. After this correction, walking became smooth.

There is INA219 current sensor code in firmware, but I removed it in the actual build to keep things simple.

Assembly Instructions (Important)
Step 1 – Print Parts

Print all STL files:

Body

Lid

Hip (L + R)

Ham (L + R)

Shank

Servo brackets

Tendon pins

Step 2 – Prepare Joints

Press M3 and M2.5 threaded inserts into body and lid

Assemble each leg

Hip → Ham (servo mounted)

Ham → Shank (M3 screw + lock nut)

Make tendons using straightened paper clips

Step 3 – Mount Servos

2 servos per leg → total 8 servos

Hip servo = top joint

Knee servo = bottom joint

Center all servo horns before tightening

Step 4 – Electronics Setup

Mount ESP32 on PCB or holder

Connect all servos to correct headers

Connect DC-DC converter and battery holder

Recheck 5V output before connecting servos

Step 5 – Final Assembly

Insert PCB and battery from bottom opening

Arrange wiring neatly inside

Close body using printed lid and screws

Step 6 – Upload Code

Connect ESP32 using USB

Upload firmware

Adjust servo trim values

Step 7 – Test & Tune

Test each leg separately

Balance robot on flat surface

Run walking code

Fine tune servo angles

Bill of Materials (BOM)
Component	Qty	Purpose
ESP32 Dev Board	1	Main controller
Servo Motors (MG90S / MG996R)	8	Leg movement
3D Printed Parts	1 Set	Frame and joints
Dual 18650 Battery Holder	1	Power supply
18650 Li-ion Battery	2	7.4V input
DC-DC Converter (5V)	1	Servo power
M3 Screws	Set	Joints & frame
M2 / M2.5 Screws	Set	PCB mounting
Threaded Inserts	Set	Strong joints
Dupont Wires	Few	Signal connections
Paper Clips	4	Tendon links
Custom PCB (optional)	1	Cleaner wiring
Update – Version 2 PCB

In the second PCB version:

Each leg has connectors for all 3 servo positions

Hip servos use B headers

Knee servos use G headers

A headers are unused

Because of this change, no pin swapping is required in software.

Conclusion

This project was not easy but very satisfying. I faced mistakes in PCB wiring, servo placement and mechanical strength, but learned a lot from fixing them. Oreo is a simple but reliable quadruped robot and can be a good starting point for anyone interested in walking robots.
