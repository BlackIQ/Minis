#include "Arduino.h"
#include "BlackIQ.h"

BlackIQ::BlackIQ(int SS_PIN , RST_PIN)
{
  
}


void BlackIQ::RFID_Board()
{
  // Run Init
  lcd.setCursor(6 , 0);
  lcd.print("RFID");
  lcd.setCursor(5 , 1);
  lcd.print("Reader");
  
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
  else {
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

  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
}
