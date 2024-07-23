int obstacle0 = 10;
int obstacle2 = 28;
int dir11 =50;
int dir12 = 46;
int dir21 = 26;
int dir22 = 34;
int pwm11 = 5;
int pwm12 = 4;
int pwm21 = 2;
int pwm22 = 3;
char byteRead = ' ';
int area_of_blobs =0;
 void setup() {
   // put your setup code here, to run once:
   Serial2.begin(19200);
   Serial.begin(9600);
  pinMode(obstacle, INPUT);
  pinMode(dir11 , OUTPUT);
  pinMode(dir12 ,OUTPUT);
  pinMode(dir21 , OUTPUT);
  pinMode(dir22 , OUTPUT);
  pinMode(pwm11 , OUTPUT);
  pinMode(pwm12 ,OUTPUT);
  pinMode(pwm21 , OUTPUT);
  pinMode(pwm22 , OUTPUT);
 }
 
 void loop() {
   // put your main code here, to run repeatedly:
   int obstacle_state = digitalRead(obstacle0);
   int obstacle_state2 = digitalRead(obstacle2);
   /*if (obstacle_state == 0){
          Serial.println("obstcle ahead");
          obstacle();
      }
   else{
    forward();*/
   if (Serial2.available()) {
         // Read the most recent byte
         byteRead = Serial2.read();
         //Serial2.write()
         //area_of_blobs = Serial2.read();
         Serial.println(byteRead);      
        
         // ECHO the value that was read
         
         if(byteRead == 'R' ){
          right();
         // Serial.println("turn right");
         }
         else if (byteRead == 'L'){
          left();
          //Serial.println("turn left");
         }
         else if (byteRead == 'F'){
          forward();
          //Serial.println("forward");
         }
         else if (byteRead == 'l' ){
          leftslowly();
          //Serial.println("Turn left slowly");
         }
         else if (byteRead == 'r'){
          rightslowly();
          //Serial.println("Turn right slowly");
         }
         else if(byteRead == 'S'){
           stop1();
           delay(6000); 
          //Serial.println(byteRead);
         
         }
         else if(byteRead == 'T'){
            Turnaround();
         }
   }
 }
