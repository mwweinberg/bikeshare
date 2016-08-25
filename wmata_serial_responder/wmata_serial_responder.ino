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
Adafruit_NeoPixel strip = Adafruit_NeoPixel(4, PIN, NEO_GRB + NEO_KHZ800);

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
    str = Serial.readStringUntil('z');

    //if var_for_string.indexOf("String")? > 0):
      //make LED this color
      // green is 255,0,0
      // yellow is 255,255,0
      // yellow is second because if both light should be
      // yellow b/c yellow goes to the airport and is 
      // likely more important

    //first light (at station)

    // first yellow train
    if (str.indexOf('i') >= 0) {
      strip.setPixelColor(0, 255, 255, 0);
    }
    //first green train
    else if (str.indexOf('a') >= 0) {
      strip.setPixelColor(0, 255, 0, 0);
    }
    // second yellow train
    else if (str.indexOf('m') >= 0) {
      strip.setPixelColor(0, 255, 255, 0);
    }    
    //second green train
    else if (str.indexOf('e') >= 0) {
      strip.setPixelColor(0, 255, 0, 0);
    }    
    // turns off the LED if nothing here
    else {
      strip.setPixelColor(0, 0, 0, 0);
    }

    //second light (leave now)

    // first yellow train
    if (str.indexOf('j') >= 0) {
      strip.setPixelColor(1, 255, 255, 0);
    }
    //first green train
    else if (str.indexOf('b') >= 0) {
      strip.setPixelColor(1, 255, 0, 0);
    }
    // second yellow train
    else if (str.indexOf('n') >= 0) {
      strip.setPixelColor(1, 255, 255, 0);
    }
    //second green train
    else if (str.indexOf('f') >= 0) {
      strip.setPixelColor(1, 255, 0, 0);
    }    
    // turns off the LED if nothing here
    else {
      strip.setPixelColor(1, 0, 0, 0);
    }
      

    //third light (coming soon)

    // first yellow train
    if (str.indexOf('k') >= 0) {
      strip.setPixelColor(2, 255, 255, 0);
    }
    //first green train
    else if (str.indexOf('c') >= 0) {
      strip.setPixelColor(2, 255, 0, 0);
    }
    // second yellow train
    else if (str.indexOf('o') >= 0) {
      strip.setPixelColor(2, 255, 255, 0);
    }
    //second green train
    else if (str.indexOf('g') >= 0) {
      strip.setPixelColor(2, 255, 0, 0);
    }    
    // turns off the LED if nothing here
    else {
      strip.setPixelColor(2, 0, 0, 0);
    }

    //fourth light (long way off)

    // first yellow train
    if (str.indexOf('l') >= 0) {
      strip.setPixelColor(3, 255, 255, 0);
    }
    //first green train
    else if (str.indexOf('d') >= 0) {
      strip.setPixelColor(3, 255, 0, 0);
    }
    // second yellow train
    else if (str.indexOf('p') >= 0) {
      strip.setPixelColor(3, 255, 255, 0);
    }
    //second green train
    else if (str.indexOf('h') >= 0) {
      strip.setPixelColor(3, 255, 0, 0);
    }    
    // turns off the LED if nothing here
    else {
      strip.setPixelColor(3, 0, 0, 0);
    }

   
  }

 

  //pushes the changes to the LEDs
  strip.show();
 
}
