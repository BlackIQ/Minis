int led = 13;

void setup() {
  pinMode(led , OUTPUT);
}

void loop() {
  // turn led on
  digitalWrite(led , HIGH);
  // delay for 1 sec
  delay(1000);

   // turn led off
  digitalWrite(led , LOW);
  // delay for 1 sec
  delay(1000); 
}
