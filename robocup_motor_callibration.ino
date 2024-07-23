#define motordir1 PB12
#define motordir2 PB13
#define motorpwm1 PA8
#define motorpwm2 PA9
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(motordir1, OUTPUT);
  pinMode(motordir2, OUTPUT);
  pinMode(motorpwm1, OUTPUT);
  pinMode(motorpwm2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(motordir1, HIGH); // low,low ----> left
  digitalWrite(motordir2, LOW); // high, low ----> forward
  analogWrite(motorpwm1, 255);
  analogWrite(motorpwm2, 255);
}
