#include <Wire.h>
#include <Adafruit_BMP085.h>
#define seaLevelPressure_hPa 1013.25

Adafruit_BMP085 bmp;
int32_t prev = 0, cur;
bool first = true;
unsigned long time;

void setup() {
  Serial.begin(9600);
  if (!bmp.begin()) {
	Serial.println("No sensor");
  }
}
  
void loop() {
  if (first) {
    Serial.println(" <-- Start time");
    first = !first;
  }

  Serial.print("Pressure = ");
  cur = bmp.readPressure();
  time = millis();
  Serial.println(String(cur) + " Pa");
  Serial.print("Difference : " + String(cur-prev));
  Serial.println(", Time : " + String(time));
  prev = cur;
  
  Serial.println();
  delay(1000);
}