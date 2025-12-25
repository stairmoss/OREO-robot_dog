🔩 ASSEMBLY – OREO Robot Dog

This document explains how to physically assemble the OREO robot dog from printed parts, electronics, and firmware. The steps are written so even beginners can follow.

🧰 Tools Required

Screwdriver (for M2 / M3 screws)

3 mm drill bit

Allen key (if needed for screws)

Soldering iron (only if PCB is not pre-soldered)

Multimeter (recommended for voltage checking)

📦 Parts Checklist

Before starting, make sure you have:

All 3D-printed parts

8 servo motors (hip + knee)

ESP32 development board

Custom PCB (optional but recommended)

DC-DC buck/boost converter

Dual 18650 battery holder + batteries

M3, M2, M2.5 screws

Threaded inserts

Paper clips (for tendons)

🖨 Step 1 – 3D Print All Parts

Print the following parts from the /CAD folder:

Body

Body Lid

Hip (Left + Right)

Ham (Left + Right)

Shank

Servo brackets

Tendon pins

Printing Notes

Rotate the body upside down before slicing

Use supports only for the body

Lid prints without supports

Drill the shank joint hole using a 3 mm drill bit

🔩 Step 2 – Insert Threaded Inserts

Heat and press M3 and M2.5 threaded inserts into the body and lid

Make sure they sit flush and straight

This helps make the joints strong and reusable

🦵 Step 3 – Assemble Legs

Each leg uses 2 servos.

Leg Assembly Order

Mount hip servo inside the hip part

Attach hip to ham section

Mount knee servo

Connect ham to shank using M3 screw + lock nut

Tendons

Straighten paper clips

Insert them as tendons

Lock them using printed tendon pins

Repeat this for all 4 legs.

⚙ Step 4 – Servo Preparation

Center all servo horns using servo tester or code

Only then screw the horns in place

This avoids uneven movement later

🔌 Step 5 – Electronics Assembly
PCB & ESP32

Mount ESP32 on PCB or holder

Fix PCB inside the body using M2 screws

Power

Connect battery holder to DC-DC converter

Adjust output to exactly 5V using multimeter

Only then connect servo power rail

⚠️ Do not connect servos before voltage check

🧠 Step 6 – Wiring

Connect hip servos to Hip headers

Connect knee servos to Knee headers

Ensure correct orientation of signal, VCC, and GND

Route wires neatly to avoid joint stress

🧩 Step 7 – Final Body Assembly

Insert PCB and battery pack through bottom opening

Arrange wires so lid closes easily

Attach lid using screws

Check leg movement by hand

💻 Step 8 – Upload Firmware

Connect ESP32 using USB

Open firmware from /Firmware folder

Install required libraries

Upload code

Set servo trim values in config file

🐾 Step 9 – Testing & Tuning

Power on robot

Test each leg individually

Place robot on flat surface

Run walking function

Adjust angles until movement is smooth

Do not rush this step, tuning is important.

✅ Assembly Complete

If all steps are followed correctly, OREO should stand properly and walk with stable movement.

ℹ Notes

Minor adjustments are normal

Servo angles differ slightly between units

Always disconnect power while fixing mechanical parts
