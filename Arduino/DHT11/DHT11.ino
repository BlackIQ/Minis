/*
    Temp , Hummid Sensor + LCD 16 x 2 char + I2C Driver
    Writeen by Amirhossein Mohammadi .

    Github.com/BlackIQ
*/

// Include Libs
#include "DHT.h"        // Temp , Humid Sensor { DHT }
#include <LiquidCrystal_I2C.h>    // Liquid Crystal Lib { LCD }
#include <Wire.h>                 // Wire lib        { I2C Driver }

// Define main DHT11 data
#define DHTPIN A0           // DHT11 Pin
#define DHTTYPE DHT11       // DHT11 Model

// Set Module and Sensor
DHT dht(DHTPIN, DHTTYPE);            // Set DHT
LiquidCrystal_I2C lcd(0x27,16,2);    // set the LCD address to 0x27 for a 16 chars and 2 line display

// Setup void
void setup() {
    // Begin
    Serial.begin(9600);     // Begin Serial
    dht.begin();            // Begin DHT
    lcd.init();             // LCD
    lcd.backlight();        // Light the backlight
}

// Main Temperature & Humidity Function
void loop() {
    // Values
    float temp = dht.readTemperature();      // Temp value
    float hum = dht.readHumidity();          // Humid value

    // Print Temp
    lcd.setCursor(0, 0);
    lcd.print("Temp  : ");
    lcd.print(temp);
    lcd.print(" C");

    // Print Humid
    lcd.setCursor(0, 1);
    lcd.print("Humid : ");
    lcd.print(hum);
    lcd.print(" %");

    // 1 Sec Delay
    delay(1000);
}