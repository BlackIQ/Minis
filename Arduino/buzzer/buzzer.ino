int buzzer = 8;

void setup() {
  pinMode(buzzer , OUTPUT);
}

void loop() {
  tone(buzzer, 500, 500);
  delay(1000);
}
