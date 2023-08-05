#define led 13

void setup() {
  pinMode(led , OUTPUT);
}

void loop() {
  digitalWrite(led , HIGH);
}
