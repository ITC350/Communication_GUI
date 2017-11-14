#include <SoftwareSerial.h>
SoftwareSerial BTserial(8, 9); // RX | TX
 
const long baudRate = 9600;

void setup() 
{
    Serial.begin(9600);
    Serial.print("Sketch:   ");   Serial.println(__FILE__);
    Serial.print("Uploaded: ");   Serial.println(__DATE__);
    Serial.println(" ");
 
    BTserial.begin(baudRate);  
    Serial.print("BTserial started at "); Serial.println(baudRate);
    Serial.println(" ");
}

char c;

void loop()
{
 /*
 if (BTserial.available()) {
   c = BTserial.read();
 }
 
 if (c == 'H') {
   Serial.println("Message received!"); 
 }
 */
 
 BTserial.write('H');
 
 delay(100);
}
