#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

const int en = 2 , rw = 1 , rs = 0 , d4 = 4 , d5 = 5 , d6 = 6 , d7 = 7 , bl = 3;

const int i2c_addr = 0x3F;

LiquidCrystal_I2C lcd(i2c_addr , en , rw , rs , d4 , d5 , d6 , d7 , bl);

void setup()
{
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.print("BlackIQ");

  delay(1000);

  lcd.setCursor(0,1);
  lcd.print("Amir !");

  delay(2000);

  lcd.clear();
}


void loop()
{
  lcd.print("BlackIQ");
}
