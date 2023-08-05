/*
  DHT11 :
  pin ~> Analog 0

  RFID LED :
  SS 10
  RST 9
  Green ~> 7
  Red ~> 6
  
*/

// Include Libs
#include <LiquidCrystal_I2C.h>
#include <DS3231.h>
#include <Wire.h>
#include "MFRC522.h"
#include "DHT.h"
#include "SPI.h"

// RFID Setup Pins
#define SS_PIN 10
#define RST_PIN 9

// DHT Setup Pins
#define DHTPIN A0
#define DHTTYPE DHT11

// Lights
#define green 7
#define red 6

// Sensors Setup
LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display
DHT dht(DHTPIN, DHTTYPE);          // DHT
DS3231 rtc(SDA , SCL);             // RTC
MFRC522 rfid(SS_PIN, RST_PIN);     // RFID
MFRC522::MIFARE_Key key;           // RFID

void setup() {

  Serial.begin(9600);  // Serial Monitor Begin

  // Begin Sensors & Modules
  dht.begin();      // DHT
  rtc.begin();      // RTC
  lcd.init();       // LCD
  rfid.PCD_Init();  // RFID
  SPI.begin();      // RFID

  lcd.backlight(); // Light the backlight

  // RFID Lights Setup
  pinMode(green , OUTPUT); // Green for available RFID Tag
  pinMode(red , OUTPUT);   // Red for Forbidden RFID Tag

  // RTC Setup
  rtc.setDOW(TUESDAY);       // Set Day-of-Week to SUNDAY
  rtc.setTime(10, 20, 0);    // Set the time to 12:00:00 (24hr format)
  rtc.setDate(7, 9, 2020);   // Set the date to January 1st, 2014

}

// LCD RFID init
void first() {
  lcd.setCursor(6 , 0);
  lcd.print("RFID");
  lcd.setCursor(5 , 1);
  lcd.print("Reader");
}

// LCD RFID Condition , If Yes
void yes() {
  lcd.setCursor(0 , 1);
  lcd.print("Available .");
  digitalWrite(green , HIGH);
  delay(5000);
  lcd.clear();
  lcd.setCursor(0 , 0);
  lcd.print("Welcome To ,");
  lcd.setCursor(0 , 1);
  lcd.print("BlackIQs Landing");
  delay(5000);
  lcd.clear();
  digitalWrite(green , LOW);
}

//LCD RFID Condition , If No
void no() {
  lcd.setCursor(0 , 1);
  lcd.print("Forbidden .");
  digitalWrite(red , HIGH);
  delay(5000);
  lcd.clear();
  lcd.setCursor(0 , 0);
  lcd.print("Walk Away ,");
  lcd.setCursor(0 , 1);
  lcd.print("Blah Blah Blah !");
  delay(5000);
  lcd.clear();
  digitalWrite(red , LOW);
}

// Marin RFID Function
void rfid_board() {
  // Run Init
  first();
  
  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
    return;

  MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);

  if (piccType != MFRC522::PICC_TYPE_MIFARE_MINI &&
    piccType != MFRC522::PICC_TYPE_MIFARE_1K &&
    piccType != MFRC522::PICC_TYPE_MIFARE_4K) {
    Serial.println(F("Your tag is not of type MIFARE Classic ."));
    return;
  }

  // Getting Tag ID
  String strID = "";
  for (byte i = 0; i < 4; i++) {
    strID +=
    (rfid.uid.uidByte[i] < 0x10 ? "0" : "") +
    String(rfid.uid.uidByte[i], HEX) +
    (i!=3 ? ":" : "");
  }
  
  strID.toUpperCase();

  // Print The ID
  lcd.setCursor(0 , 0);
  lcd.print("ID : ");
  lcd.print(strID);

  // Condiotion
  if (strID.indexOf("63:19:BA:3E") >= 0) {
    yes();
  }
  else {
    no();
  }

  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
}

// Main Real Time Clock Function
void RealTimeClock() {

  // Values
  String tim = rtc.getTimeStr();
  String dat = rtc.getDateStr();

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

// Main Temperature & Humidity Function
void TumpHumid() {

  // Values
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

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

// Main Arduino Loop
void loop() {

  // Here , You can comment and uncomment Voids

//  TumpHumid();
//  RealTimeClock();
  rfid_board();
    
}
