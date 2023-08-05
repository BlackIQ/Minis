/*
    LCD 16 x 2 Char + I2C Driver
    Writeen by Amirhossein Mohammadi .

    Github.com/BlackIQ
*/

// Include Libs
#include <LiquidCrystal_I2C.h>    // Liquid Crystal Lib { LCD }
#include <Wire.h>                 // Wire lib        { I2C Driver }

// Set Modules
LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display
DS3231 rtc(SDA , SCL);             // RTC

// Setup void
void setup() {
    // Begin
    Serial.begin(9600);   // Begin Serial
    lcd.init();           // LCD
    lcd.backlight();      // Light the backlight
}

// Main Real Time Clock Function
void loop() {
    // Print on line 1
    lcd.setCursor(0, 0);
    lcd.print("Hi Git !");

    // Print on line 2
    lcd.setCursor(0, 1);
    lcd.print("I Love Arduino !");
}