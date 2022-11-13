/*
 * Binary counter with controllable frequency, mainly inspired by
 * https://create.arduino.cc/projecthub/Madhur_Bajpai/binary-counter-using-leds-2089d9
 * Author: Bryan Ngo, Fall 2022 HKN Serv Officer
 */

// initialize LED output pins
int pin1 = A0;
int pin2 = A1;
int pin3 = A5;
int pin4 = 21;

// initialize potentiometer output pin
int pot_in = A7;

// initialize rolling counter
int i = 0;

void setup() {
  // put your setup code here, to run once:

  /*
   * tell the microcontroller these pins
   * will be outputs rather than inputs
   */
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  pinMode(pin4, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  // increment counter
  i++;

  // take a measurement from the potentiometer
  int pot_read = analogRead(pot_in);

  // check if pin 1 should be on (if even number)
  if ((i % 2) > 0) {
    digitalWrite(pin1, HIGH);
  } else {
    digitalWrite(pin1, LOW);
  }

  /* check if pin 2 should be on 
   * (if has a 2 in its binary expansion)
   */
  if ((i % 4) > 1) {
    digitalWrite(pin2, HIGH);
  } else {
    digitalWrite(pin2, LOW);
  }

  /* check if pin 3 should be on
   * (if has an 4 in its binary expansion)
   */
  if ((i % 8) > 3) {
    digitalWrite(pin3, HIGH);
  } else {
    digitalWrite(pin3, LOW);
  }

  /* check if pin 4 should be on
   * (if has an 8 in its binary expansion)
   */
  if ((i % 16) > 7) {
    digitalWrite(pin4, HIGH);
  } else {
    digitalWrite(pin4, LOW);
  }

  // scale analog reading & clip minimum frequency
  delay(max(pot_read / 10, 50));
}
