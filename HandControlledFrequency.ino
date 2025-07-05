int buzzPin = 6, ledPin = 9;
int length, signal;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(buzzPin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    length = (Serial.readStringUntil('\r')).toInt();
  }

  signal = map(length, 30, 300, 0, 255);

  if (length >= 30 && length <= 300) {
    analogWrite(ledPin, signal);
    analogWrite(buzzPin, signal);
  }
  else {
    analogWrite(ledPin, 0);
    analogWrite(buzzPin, 0);
  }
}
