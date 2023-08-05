#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27 , 16 , 2);

void setup() {
  lcd.init();
  lcd.backlight();
}


void loop() {
  lcd.setCursor(0 , 0);
  lcd.print("Counter :");

  int counter = 0;

  while (true) {
    lcd.setCursor(0 , 1);
    lcd.print(counter);
    counter++;
    delay(1000);
  }
  
}
