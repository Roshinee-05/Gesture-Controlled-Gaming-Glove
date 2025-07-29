#include <Wire.h>
#include <math.h>
const int MPU_addr = 0x68;
int16_t AcX, AcY, AcZ;
double xAngle, yAngle;
bool allowW = true, allowA = true, allowS = true, allowD = true;

4

void setup() {
Wire.begin();
Wire.beginTransmission(MPU_addr);
Wire.write(0x6B); // Wake up MPU6050
Wire.write(0);
Wire.endTransmission(true);
Serial.begin(9600);
}
void loop() {
Wire.beginTransmission(MPU_addr);
Wire.write(0x3B); // Start register
Wire.endTransmission(false);
Wire.requestFrom(MPU_addr, 6, true); // Read accelerometer
data
AcX = Wire.read() << 8 | Wire.read();
AcY = Wire.read() << 8 | Wire.read();
AcZ = Wire.read() << 8 | Wire.read();
// Convert raw data to angles
xAngle = atan2(AcY, AcZ) * 180 / PI;
yAngle = atan2(-AcX, sqrt(AcY * AcY + AcZ * AcZ)) * 180 / PI;
// Debug (optional)
// Serial.print("X: "); Serial.print(xAngle);
// Serial.print(" | Y: "); Serial.println(yAngle);
// Forward - W
if (yAngle > 20 && allowW) {
Serial.println("KEY_W");
allowW = false;
} else if (yAngle < 15) {
allowW = true;
}
// Backward - S

5
if (yAngle < -20 && allowS) {
Serial.println("KEY_S");
allowS = false;
} else if (yAngle > -15) {
allowS = true;
}
// Left - A
if (xAngle < -20 && allowA) {
Serial.println("KEY_A");
allowA = false;
} else if (xAngle > -15) {
allowA = true;
}
// Right - D
if (xAngle > 20 && allowD) {
Serial.println("KEY_D");
allowD = false;
} else if (xAngle < 15) {
allowD = true;
}
delay(100);
}
