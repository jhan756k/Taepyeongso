#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;
int32_t prev = 0;
double pas, atm;
double DELTA_T = 0.1, time = 0.0;

void setup() {
  Serial.begin(9600);
  if (!bmp.begin()) {
    Serial.println("No sensor");
  }
}

void loop() {
  pas = bmp.readPressure();
  atm = pas/101325.0;
  Serial.print(String(pas) + " Pa, ");
  Serial.println(String(atm) + " atm");
  Serial.print("Difference : " + String(pas - prev));
  Serial.println(", Time : " + String(time));
  prev = pas;
  time += DELTA_T;

  Serial.println();
  delay(DELTA_T * 1000);
}