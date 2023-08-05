/*
    LCD 16 x 2 Char + I2C Driver
    Writeen by Amirhossein Mohammadi .

    Github.com/BlackIQ
*/

// Include Libs
#include <DS3231.h>               // Real Time Clock { Clock Module }
#include <LiquidCrystal_I2C.h>    // Liquid Crystal Lib { LCD }
#include <Wire.h>                 // Wire lib        { I2C Driver }

// Set Modules
LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display
DS3231 rtc(SDA , SCL);             // RTC

// Setup void
void setup() {
    // Begin
    Serial.begin(9600);   // Begin Serial
    rtc.begin();          // Begin RTC
    lcd.init();           // LCD
    lcd.backlight();      // Light the backlight

    // RTC Setup
    rtc.setDOW(TUESDAY);       // Set Day-of-Week to SUNDAY
    rtc.setTime(10, 20, 0);    // Set the time to 12:00:00 (24hr format)
    rtc.setDate(7, 9, 2020);   // Set the date to January 1st, 2014
}

// Main Real Time Clock Function
void loop() {
  // Values
  String tim = rtc.getTimeStr();         // Time value
  String dat = rtc.getDateStr();         // Date value

  // Print Time
  lcd.setCursor(0, 0);
  lcd.print("Time: ");
  lcd.print(tim);

  // Print Date
  lcd.setCursor(0, 1);
  lcd.print("Date: ");
  lcd.print(dat);

  // 1 Sec Delay
  delay(1000);
}