#include <Stepper.h>

// float xy_speed z_speed;
const int spr = 64;//Steps Per Revolution

// Initialize Stepper Motors
Stepper x_motor(spr,2,4,3,5);
Stepper y_motor(spr,6,8,7,9);
Stepper z_motor(spr,10,12,11,13);

void setup() {
  Serial.begin(9600);
  delay(2000);
  Serial.println("Arduino Connected!");

  //Set motor speeds
  x_motor.setSpeed(200);
  y_motor.setSpeed(200);
  z_motor.setSpeed(200);


}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    String command = Serial.readString();
    Serial.println(command);
    if(command.equals("x_pos_btn")){
      Serial.println("X+ button pressed");
      x_motor.step(500);
    }
    else if(command.equals("x_neg_btn")){
      Serial.println("X- button pressed");
      x_motor.step(-500);
    }
    else if(command.equals("y_pos_btn")){
      Serial.println("Y+ button pressed");
      y_motor.step(500);
    }
    else if(command.equals("y_neg_btn")){
      Serial.println("Y- button pressed");
      y_motor.step(-500);
    }
      
      
      
    
  }
  // x_motor.step(3000);
  // delay(1000);
}
