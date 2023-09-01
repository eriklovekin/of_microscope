#include <Stepper.h>

// float xy_speed z_speed;
const int spr = 64;//Steps Per Revolution

// Initialize Stepper Motors
Stepper x_motor(spr,2,3,4,5);
Stepper y_motor(spr,6,7,8,9);
Stepper z_motor(spr,10,11,12,13);

void setup() {
  Serial.begin(9600);
  Serial.print('Arduino Connected');

  //Set motor speeds
  x_motor.setSpeed(200);
  y_motor.setSpeed(3);
  z_motor.setSpeed(3);


}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    int command = Serial.read();
    Serial.print(command, DEC);
  }
  // x_motor.step(3000);
  // delay(1000);
}
