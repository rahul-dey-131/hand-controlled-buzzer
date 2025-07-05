int buzzPin = 7;
int length, freq;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(buzzPin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    length = (Serial.readStringUntil('\r')).toInt();
  }

  if (length >= 30 && length <= 240) {
    buzz(length);
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(buzzPin, LOW);
    digitalWrite(13, LOW);
  }
  // delay(0.25);
}

void buzz(int length) {
  freq = map(length, 30, 240, 20, 2000);
  float period = 1000000.0 / freq;
  unsigned long duration = 250000;  // 50ms

  for (unsigned long t = 0; t < duration; t += period) {
    digitalWrite(buzzPin, HIGH);
    delayMicroseconds(period / 2);
    digitalWrite(buzzPin, LOW);
    delayMicroseconds(period / 2);
  }
}
