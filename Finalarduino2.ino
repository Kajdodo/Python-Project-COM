int motorrechts = 5;
int motorlinks = 6;
int sensorValuepot = analogRead(A0);
int sensorValuepos = analogRead(A1);
int cilinder = 2;
int rood = 3;
int groen = 4;
int aantal;
int i;
char s;
int tel = 0;
int posities[8];
void setup()
{
  Serial.begin(9600);
  pinMode(groen, OUTPUT);
  pinMode(rood, OUTPUT);
  pinMode(motorlinks, OUTPUT);
  pinMode(motorrechts, OUTPUT);
  pinMode(cilinder, OUTPUT);
}

void loop()
{
  int posities[10];
  int aantal;
  int sensorValuepot = analogRead(A0);
  int sensorValuepos = analogRead(A1);




  if (Serial.available() > 0) {
    posities[i] = Serial.parseInt();
    Serial.println(posities[i]);

    switch (posities[i]) {
      
      case 1:
      
        cilinder_uit();
        
        while (sensorValuepot > 100) {
          sensorValuepot = analogRead(A0);
        }
     
          delay(1000);
          rood_aan();
          delay(2000);
          rood_uit();
          delay(2000);
          cilinder_in();
          delay(500);
          motor_rechts();
          delay(1000);

        while (tel < 5) {
          sensorValuepos = analogRead(A1);
          delay(150);
          if (sensorValuepos < 100) {
            tel = tel + 1;
            Serial.println(tel);

          }
        }
        
          stoppen();
          delay(500);
          cilinder_uit();
          delay(1000);
          groen_aan();
          delay(2000);
          groen_uit();

        while (sensorValuepot < 100) {
          sensorValuepot = analogRead(A0);
        }
        
          delay(2000);
          cilinder_in();
          delay(500);
          motor_links();
          delay(1000);

        while (tel < 10) {
          sensorValuepos = analogRead(A1);
          delay(150);
          if (sensorValuepos < 100) {
            tel = tel + 1;
            Serial.println(tel);
          }
        }

          stoppen();
          delay(3000);
          tel = 0;

        break;



        
      case 2:
      
        cilinder_uit();
        
        while (sensorValuepot > 100) {
          sensorValuepot = analogRead(A0);
        }
        
          delay(1000);
          rood_aan();
          delay(2000);
          rood_uit();
          delay(2000);
          cilinder_in();
          delay(500);
          motor_links();
          delay(1000);

        while (sensorValuepos > 100) {
          sensorValuepos = analogRead(A1);
        }
        
          stoppen();
          delay(500);
          cilinder_uit();
          delay(1000);
          groen_aan();
          delay(2000);
          groen_uit();
        
        while (sensorValuepot < 100) {
          sensorValuepot = analogRead(A0);
        }
       
          delay(2000);
          cilinder_in();
          delay(500);
          motor_rechts();
          delay(1000);
          sensorValuepos = 1000;

        while (sensorValuepos > 100) {            
          sensorValuepos = analogRead(A1);
        }
       
          stoppen();
          delay(3000);

        break;





      case 4:
      
        cilinder_uit();
        
        while (sensorValuepot > 100) {
          sensorValuepot = analogRead(A0);
        }

          delay(1000);
          rood_aan();
          delay(2000);
          rood_uit();
          delay(2000);
          cilinder_in();
          delay(500);
          motor_rechts();
          delay(1000);

        while (sensorValuepos > 100) {
          sensorValuepos = analogRead(A1);
        }
          
          stoppen();
          delay(500);
          cilinder_uit();
          delay(1000);
          groen_aan();
          delay(2000);
          groen_uit();

        while (sensorValuepot < 100) {
          sensorValuepot = analogRead(A0);
        }
       
          delay(2000);
          cilinder_in();
          delay(500);
          motor_links();
          delay(1000);
          sensorValuepos = 1000;               

        while (sensorValuepos > 100) {             
          sensorValuepos = analogRead(A1);
        }
       
          stoppen();
          delay(3000);
          
        break;





        
      case 3:
      
        cilinder_uit();
        
        while (sensorValuepot > 100) {
          sensorValuepot = analogRead(A0);
        }
      
          delay(1000);
          rood_aan();
          delay(2000);
          rood_uit();
          delay(2000);
          cilinder_in();
          delay(500);
          motor_rechts();
          delay(1000);

        while (tel < 3) {
          sensorValuepos = analogRead(A1);
          delay(150);
          if (sensorValuepos < 100) {
            tel = tel + 1;
            Serial.println(tel);

          }
        }

          stoppen();
          delay(500);
          cilinder_uit();
          delay(1000);
          groen_aan();
          delay(2000);
          groen_uit();
 
        while (sensorValuepot < 100) {            
          sensorValuepot = analogRead(A0);
        }
        
          delay(2000);
          cilinder_in();
          delay(500);
          motor_links();
          delay(1000);
        
        while (tel < 6) {
          sensorValuepos = analogRead(A1);
          delay(150);
          if (sensorValuepos < 100) {
            tel = tel + 1;
            Serial.println(tel);
          }
        }
        
          stoppen();
          delay(3000);
 
        break;
    }
    Serial.read();
  }
}


void motor_links()
{
  int sensorValue = analogRead(A0);
  int motorrechts = 5;
  int motorlinks = 6;

  analogWrite(motorrechts, 0);
  analogWrite(motorlinks, 65);
}


void motor_rechts()
{
  int sensorValue = analogRead(A0);
  int motorrechts = 5;
  int motorlinks = 6;
  analogWrite(motorrechts, 65);
  analogWrite(motorlinks, 0);
}


void stoppen()
{
  int motorrechts = 5;
  int motorlinks = 6;
  analogWrite(motorrechts, 0);
  analogWrite(motorlinks, 0);
}


void cilinder_in()
{
  int cilinder = 2;
  digitalWrite(cilinder, LOW);
}


void cilinder_uit()
{
  int cilinder = 2;
  digitalWrite(cilinder, HIGH);
}


void groen_aan()
{
  digitalWrite(groen, HIGH);
}

void groen_uit()
{
  digitalWrite(groen, LOW);
}

void rood_aan()
{
  digitalWrite(rood, HIGH);
}

void rood_uit()
{
  digitalWrite(rood, LOW);
}
