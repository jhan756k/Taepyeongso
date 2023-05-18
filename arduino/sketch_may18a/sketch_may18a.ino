#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;
int32_t prev = 0, cur;
double DELTA_T = 1, time = 0.0;

void setup() {
  Serial.begin(9600);
  if (!bmp.begin()) {
    Serial.println("No sensor");
  }
}

void loop() {
  Serial.print(time);
  Serial.println(bmp.readPressure());
  Serial.print(cur-prev);
  prev = cur;
  time += DELTA_T;

  Serial.println();
  delay(DELTA_T * 1000);
}