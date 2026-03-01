#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <MPU6050_tockn.h>

// PCA9685 setup
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
#define SERVO_FREQ 50 // Analog servos run at ~50Hz

// IMU setup
MPU6050 mpu6050(Wire);

// Failsafe variables
unsigned long lastCommandTime = 0;
const unsigned long FAILSAFE_TIMEOUT = 2000; // 2 seconds
bool isFailsafe = false;

// Servo Pulse constants (Adjust based on your 20kg servos)
#define SERVOMIN  150 // Minimum pulse length count (out of 4096)
#define SERVOMAX  500 // Maximum pulse length count (out of 4096)

void setup() {
  Serial.begin(115200);
  Wire.begin();
  
  // Initialize PCA9685
  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);

  // Initialize IMU
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);

  delay(10);
  lastCommandTime = millis();
}

// Convert degrees (0-180) to PCA9685 pulse
int degToPulse(int deg) {
  return map(deg, 0, 180, SERVOMIN, SERVOMAX);
}

void enterFailsafe() {
  if (!isFailsafe) {
    // Move to "Sit" position (Example: all legs 90 or specific angles)
    for (int i = 0; i < 16; i++) {
      pwm.setPWM(i, 0, 4096); // This turns off the pulse to "detach"
    }
    isFailsafe = true;
  }
}

void loop() {
  // 1. Handle Serial Input from Raspberry Pi
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if (data.startsWith("S,")) {
      isFailsafe = false;
      lastCommandTime = millis();
      
      // Parse CSV: S,a1,a2,a3...a12
      int angles[12];
      int currentIndex = 0;
      int startPos = 2; // Skip "S,"
      
      for (int i = 0; i < 12; i++) {
        int commaPos = data.indexOf(',', startPos);
        if (commaPos != -1) {
          angles[i] = data.substring(startPos, commaPos).toInt();
          startPos = commaPos + 1;
        } else {
          angles[i] = data.substring(startPos).toInt();
        }
        
        // Write to PCA9685 (Channels 0-11)
        pwm.setPWM(i, 0, degToPulse(angles[i]));
      }
    }
  }

  // 2. Failsafe Logic
  if (millis() - lastCommandTime > FAILSAFE_TIMEOUT) {
    enterFailsafe();
  }

  // 3. Stream IMU Data to Pi (50Hz)
  static unsigned long lastIMUTime = 0;
  if (millis() - lastIMUTime > 20) {
    mpu6050.update();
    Serial.print("IMU,");
    Serial.print(mpu6050.getAngleX()); // Pitch
    Serial.print(",");
    Serial.println(mpu6050.getAngleY()); // Roll
    lastIMUTime = millis();
  }
}