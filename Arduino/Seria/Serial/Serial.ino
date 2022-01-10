#define led 13

void setup() {
  Serial.begin(9600);
  pinMode(led , OUTPUT);
}

void loop() {
  for (int i=0; true; i++) {
    Serial.print("Loop Number : ");
    Serial.println(i);
    delay(1000);
    Serial.println("Light Is On . . .");
    digitalWrite(led , HIGH);
    delay(1000);
    digitalWrite(led , LOW);
    Serial.println("Light Is Off .");
    delay(3000);
  }
}
