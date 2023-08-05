#define relay 11

void setup() {
  pinMode(relay , OUTPUT);
}

void loop() {
  digitalWrite(relay , HIGH);
  delay(5000);
  digitalWrite(relay , LOW);
  delay(5000);
}
