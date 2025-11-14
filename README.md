# OREO-robot_dog
Oreo is a small 3D-printed robot dog powered by an ESP32 and lightweight servo legs. Its compact body, strong joints, and simple two-servo leg design give it smooth, stable movement. With a clean internal layout for the battery and PCB, Oreo is built for easy assembly, testing, and fun robotics experiments.




I designed my own compact robot dog based on a fully customized 3D-printed frame, optimised joints, and simplified electronics. My goal was to create a stable, lightweight, and beginner-friendly quadruped that uses only two servos per leg—one for the hip and one for the knee—while keeping the entire system clean and modular.

The leg design originally used three servos (Alpha, Beta, Gamma). I reconfigured the structure to run on just the hip and knee servos. While preparing the electronics, I discovered that I connected the wrong servo positions on the PCB, so I reordered the servo pin configuration inside the main config file. After this correction, the robot walked as expected with smooth movement.

3D Printing

I redesigned the frame to use screws instead of filament-based hinge pins so the joints are stronger and last longer.
The entire body prints nearly as one piece, with a rectangular opening on the underside for the battery pack and access to the main PCB.

Printing Notes

Rotate the body upside down before slicing so the large opening faces upward.

Print with supports under the overhangs.

The lid prints without supports.

The body uses threaded inserts to hold the lid and hips firmly.

Hip components and ham sections must be printed twice each (left + right).

The shank hole requires a 3mm drill for the joint screw.

Tendons are made from straightened paper clips and are locked using printed pins.

PCB

For durability, I added a full-size USB Type-B port so I don’t have to rely on the tiny USB connector on the ESP32 board.
I repurposed an old USB cable by adding a 4-pin connector so it fits neatly into my PCB layout.

A DC-DC boost regulator powers the servos. I set the regulator output to 5V before soldering to avoid overvoltage damage.
My PCB is fixed inside the body using four M2 screws.

Software

I run custom firmware for gait control and servo synchronization. Because of my initial servo-pin mismatch, I modified the leg configuration file to swap hip and knee servo pins for all four legs.

An INA219 current sensor driver exists in the firmware, but I removed that feature in my build because I’m keeping the design minimal.

Conclusion

This build was challenging but extremely satisfying. The mechanics, PCB, and firmware all came together to form a reliable little robot dog. Anyone who wants to explore quadruped robotics can use this concept as a starting point.

Update V2

I revised the schematic and PCB again so each leg now has full connectors for all three servo positions. This means:

Hip servos use the B headers

Knee servos use the G headers

A headers are unused
With this change, no manual pin swapping is required in software.

Custom Parts & Enclosures

I created STL files for:

Full body

Body lid

Hip left/right

Ham left/right

Shank

Servo brackets

Tendon pins

Schematics

I drafted:

Schematic V1

PCB V1

Schematic V2 (with upgraded servo layout)

PCB V2

Code

My firmware handles:

Leg IK

Servo mapping

Timing control

Basic walking gait






















Oreo Robot Dog – Components Table
Component	Qty	Purpose
ESP32 Dev Board	1	Main controller for Oreo
MG90S / MG996R Servo	8	Hip + knee movement for all 4 legs
3D-printed Body Parts	1 full set	Frame, legs, joints
Dual 18650 Battery Holder	1	Power supply for servos & ESP32
18650 Li-ion Batteries	2	7.4V power source
DC-DC Buck/Boost Converter (5V Output)	1	Stable 5V power for servos
M3 Screws (6mm, 20mm)	Set	For joints & body assembly
M2 / M2.5 Screws	Set	Mounting PCB + battery holder
Threaded Inserts (M3 + M2.5)	Set	For securing body and lid
Dupont Jumper Wires	Several	Servo & power connections
Paper Clips (medium size)	4	For tendon linkages
Custom PCB (optional)	1	Clean wiring & USB port
How to Build Oreo – Simple Steps
1. Print the 3D Parts

Print the body, lid, hips, hams, shanks, and tendon pins.

Rotate the body upside down before slicing.

Use supports only for the body.

Drill the shank–ham joint hole with a 3mm drill.

2. Prepare the Joints

Press M3 and M2.5 threaded inserts into the body and lid.

Assemble each leg:

Hip → Ham (servo mounted)

Ham → Shank (M3 screw + locknut)

Tendons are made from straightened paper clips and held with printed pins.

3. Mount the Servos

2 servos per leg → 8 total.

Hip servo = upper joint

Knee servo = lower joint

Make sure all horns are centered before screwing in.

4. Install Electronics

Place the ESP32 board on the PCB or mount surface.

Connect servos to their respective pins (Hip, Knee).

Connect battery holder + DC converter to supply 5V to all servos.

Ensure buck converter is calibrated to exactly 5V.

5. Fit Everything Inside the Body

Insert the PCB through the bottom opening.

Insert the battery pack.

Close using the printed lid + small screws.

6. Upload Firmware

Connect ESP32 via USB.

Install required servo-control library.

Upload the walking code.

Adjust servo trim values to make Oreo stand straight.

7. Test & Tune

Test each leg individually.

Balance Oreo on all four legs.

Run the walking function.

Adjust angles until walking becomes smooth.  
