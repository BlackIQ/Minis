#include <Wire.h>
#include <DS3231.h>
 
struct ts t; 
 
void setup() {
  Serial.begin(9600);
  Wire.begin();
  DS3231_init(DS3231_INTCN);
  /*----------------------------------------------------------------------------
  In order to synchronise your clock module, insert timetable values below !
  ----------------------------------------------------------------------------*/
  t.hour=12; 
  t.min=30;
  t.sec=0;
  t.mday=25;
  t.mon=12;
  t.year=2019;
 
  DS3231_set(t); 
}
 
void loop() {
  DS3231_get(&t);
  Serial.print("Date : ");
  Serial.print(t.mday);
  Serial.print("/");
  Serial.print(t.mon);
  Serial.print("/");
  Serial.print(t.year);
  Serial.print("\t Hour : ");
  Serial.print(t.hour);
  Serial.print(":");
  Serial.print(t.min);
  Serial.print(".");
  Serial.println(t.sec);
 
  delay(1000);
}
