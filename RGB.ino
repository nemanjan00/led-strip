#define INPUT_SIZE 11

int pins[] = {3, 5, 6};

int leds[3];

void setup() {
  randomSeed(analogRead(0));
  Serial.begin(115200);

  for (int i = 0; i < 3; i++) {
    leds[i] = false;
  }
}

void loop() {
  if (Serial.available()) {
    char input[INPUT_SIZE + 1];
    byte size = Serial.readBytes(input, INPUT_SIZE);
    input[size] = 0;

    char* separator = strtok(input, " \n");
    if (separator != NULL) {
      int red = String(separator).toInt();

      separator = strtok(NULL, "  \n");
      int green = String(separator).toInt();

      separator = strtok(NULL, "  \n");
      int blue = String(separator).toInt();

      analogWrite(pins[0], red);
      analogWrite(pins[1], green);
      analogWrite(pins[2], blue);

      //Serial.print(red);
      //Serial.print(" ");
      //Serial.print(green);
      //Serial.print(" ");
      //Serial.println(blue);
    }
  }
}


