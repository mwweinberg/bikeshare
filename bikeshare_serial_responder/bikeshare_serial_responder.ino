#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6
int incomingByte; //variable to read incoming serial data
String str;

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
//   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(5, PIN, NEO_GRB + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

void setup() {
 


  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
   // initialize serial communication:
  Serial.begin(9600);
}

void loop() {

  // see if there's incoming serial data:
  // TODO: read the string instead of just the most recent char
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    // TODO: make this variable the entire string
    str = Serial.readStringUntil('Z');

    //if var_for_string.indexOf("String")? > 0):
      //make LED this color

    //first station

    if (str.indexOf('A') >= 0) {
      strip.setPixelColor(0, 255, 0, 0);
    }

    if (str.indexOf('B') >= 0) {
      strip.setPixelColor(0, 255, 255, 0);
    }

    if (str.indexOf('C') >= 0) {
      strip.setPixelColor(0, 128, 255, 0);
    }

    if (str.indexOf('D') >= 0) {
      strip.setPixelColor(0, 0, 255, 0);
    }


    //second station

    if (str.indexOf('E') >= 0) {
      strip.setPixelColor(1, 255, 0, 0);
    }

    if (str.indexOf('F') >= 0) {
      strip.setPixelColor(1, 255, 255, 0);
    }

    if (str.indexOf('G') >= 0) {
      strip.setPixelColor(1, 128, 255, 0);
    }

    if (str.indexOf('H') >= 0) {
      strip.setPixelColor(1, 0, 255, 0);
    }

    //third station

    if (str.indexOf('I') >= 0) {
      strip.setPixelColor(2, 255, 0, 0);
    }

    if (str.indexOf('J') >= 0) {
      strip.setPixelColor(2, 255, 255, 0);
    }

    if (str.indexOf('K') >= 0) {
      strip.setPixelColor(2, 128, 255, 0);
    }

    if (str.indexOf('L') >= 0) {
      strip.setPixelColor(2, 0, 255, 0);
    }

    //fourth station

    if (str.indexOf('M') >= 0) {
      strip.setPixelColor(3, 255, 0, 0);
    }

    if (str.indexOf('N') >= 0) {
      strip.setPixelColor(3, 255, 255, 0);
    }

    if (str.indexOf('O') >= 0) {
      strip.setPixelColor(3, 128, 255, 0);
    }

    if (str.indexOf('P') >= 0) {
      strip.setPixelColor(3, 0, 255, 0);
    }

     //fifth station

    if (str.indexOf('Q') >= 0) {
      strip.setPixelColor(4, 255, 0, 0);
    }

    if (str.indexOf('R') >= 0) {
      strip.setPixelColor(4, 255, 255, 0);
    }

    if (str.indexOf('S') >= 0) {
      strip.setPixelColor(4, 128, 255, 0);
    }

    if (str.indexOf('T') >= 0) {
      strip.setPixelColor(4, 0, 255, 0);
    }
   
  }

 

  //pushes the changes to the LEDs
  strip.show();
 
}
