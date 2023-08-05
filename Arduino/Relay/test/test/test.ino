// Include Libs
#include "MFRC522.h"
#include "SPI.h"

// RFID Setup Pins
#define SS_PIN 10
#define RST_PIN 9

// Relay
#define in1 5

// Sensors Setup
MFRC522 rfid(SS_PIN, RST_PIN);     // RFID
MFRC522::MIFARE_Key key;           // RFID

void setup() {
  rfid.PCD_Init();  // RFID
  SPI.begin();      // RFID

  // Relay
  pinMode(in1 , OUTPUT);
}

// Main Arduino Loop
void loop() {
    if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
    return;

  MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);

  // Getting Tag ID
  String strID = "";
  for (byte i = 0; i < 4; i++) {
    strID +=
    (rfid.uid.uidByte[i] < 0x10 ? "0" : "") +
    String(rfid.uid.uidByte[i], HEX) +
    (i!=3 ? ":" : "");
  }
  
  strID.toUpperCase();

  // Condiotion
  if (strID.indexOf("63:19:BA:3E") >= 0) {
    digitalWrite(in1 , HIGH);
  }
  else {
    digitalWrite(in1 , LOW);
  }

  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
}
