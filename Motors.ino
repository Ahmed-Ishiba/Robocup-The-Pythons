 void forward(){
      analogWrite(pwm11 , 75);//top right motor
      analogWrite(pwm12 , 75);//TOP left motor 
      analogWrite(pwm21 , 75);//bottom RIGHT motor
      analogWrite(pwm22 , 75);//BOTTOM LEFT MOTOR
      digitalWrite(dir11, LOW);//LOW -->forward , high -->backwards 
      digitalWrite(dir12, HIGH);//HIGH -->forward , LOW -->backwards
      digitalWrite(dir21, HIGH);//HIGH --> Forward , LOW -->backwards
      digitalWrite(dir22, LOW);//LOW --> forward , HIGH --> backwards 
 }
 void forwardd(){
  forward();
  delay(100);
 }
 void right(){
        
     analogWrite(pwm11 , 0);//top right motor
      analogWrite(pwm12 , 0);//TOP left motor 
      analogWrite(pwm21 , 150);//bottom RIGHT motor
      analogWrite(pwm22 , 150);//BOTTOM LEFT MOTOR
      digitalWrite(dir11, HIGH);//LOW -->forward , high -->backwards 
      digitalWrite(dir12, LOW);//HIGH -->forward , LOW -->backwards
      digitalWrite(dir21, LOW);//HIGH --> Forward , LOW -->backwards
      digitalWrite(dir22, LOW);//LOW --> forward , HIGH --> backwards   // FORWARD, BACKWARD, FRWARD, BACKWARD      

 }
 void left(){
      analogWrite(pwm11 , 0);//top right motor
      analogWrite(pwm12 , 0);//TOP left motor 
      analogWrite(pwm21 , 150);//bottom RIGHT motor
      analogWrite(pwm22 , 150);//BOTTOM LEFT MOTOR
      digitalWrite(dir11, HIGH);//LOW -->forward , high -->backwards 
      digitalWrite(dir12, LOW);//HIGH -->forward , LOW -->backwards
      digitalWrite(dir21, HIGH);//HIGH --> Forward , LOW -->backwards
      digitalWrite(dir22, HIGH);//LOW --> forward , HIGH --> backwards   // FORWARD, BACKWARD, FRWARD, BACKWARD
 }
 void rightslowly(){
      analogWrite(pwm11 , 75);//top right motor
      analogWrite(pwm12 , 100);//TOP left motor 
      analogWrite(pwm21 , 75);//bottom RIGHT motor
      analogWrite(pwm22 , 100);//BOTTOM LEFT MOTOR
      digitalWrite(dir11, LOW);//LOW -->forward , high -->backwards 
      digitalWrite(dir12, HIGH);//HIGH -->forward , LOW -->backwards
      digitalWrite(dir21, HIGH);//HIGH --> Forward , LOW -->backwards
      digitalWrite(dir22, LOW);//LOW --> forward , HIGH --> backwards   //30,150,30,150 FORWARD, FORWARD, FORWAWRD,FORWAD
 }
 
 void leftslowly(){   
      analogWrite(pwm11 , 100);//top right motor
      analogWrite(pwm12 , 75);//TOP left motor 
      analogWrite(pwm21 , 75);//bottom RIGHT motor
      analogWrite(pwm22 , 100);//BOTTOM LEFT MOTOR
      digitalWrite(dir11, LOW);//LOW -->forward , high -->backwards 
      digitalWrite(dir12, HIGH);//HIGH -->forward , LOW -->backwards
      digitalWrite(dir21, LOW);//HIGH --> Forward , LOW -->backwards
      digitalWrite(dir22, LOW);//LOW --> forward , HIGH --> backwards  //100, 75, 75, 100
 }
 void stop1(){
      analogWrite(pwm11 , 0);//top right motor
      analogWrite(pwm12 , 0);//TOP left motor 
      analogWrite(pwm21 , 0);//bottom RIGHT motor
      analogWrite(pwm22 , 0);//BOTTOM LEFT MOTOR
      digitalWrite(dir11, LOW);//LOW -->forward , high -->backwards 
      digitalWrite(dir12, HIGH);//HIGH -->forward , LOW -->backwards
      digitalWrite(dir21, LOW);//HIGH --> Forward , LOW -->backwards
      digitalWrite(dir22, LOW);//LOW --> forward , HIGH --> backwards 
 }
 void backwards(){
      analogWrite(pwm11 , 75);//top right motor
      analogWrite(pwm12 , 75);//TOP left motor 
      analogWrite(pwm21 , 75);//bottom RIGHT motor
      analogWrite(pwm22 , 75);//BOTTOM LEFT MOTOR
      digitalWrite(dir11, HIGH);//LOW -->forward , high -->backwards 
      digitalWrite(dir12, LOW);//HIGH -->forward , LOW -->backwards
      digitalWrite(dir21, LOW);//HIGH --> Forward , LOW -->backwards
      digitalWrite(dir22, HIGH);// --> backwards 
 }
 void Turnaround(){
      backwards();
      delay(500);
      right();
      delay(2000);  
 }
 void obstacle(){
      backwards();
      delay(500);
      right();
      delay(750);
      leftslowly();
      delay(3000);
 }
