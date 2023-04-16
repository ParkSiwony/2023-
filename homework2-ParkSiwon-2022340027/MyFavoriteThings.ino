// F대신 F#

#define E1 329.60
#define B1 493.9
#define F1 370.0
#define B0 246.9
#define A1 440.0
#define D1 293.7
#define G1 392,0
#define C1 261.6
#define Eb 311.1
#define Empty 0

int melody[] = {
  E1, B1, B1, F1, E1, E1, B0, E1, E1, F1 ,E1, Empty,
  E1, B1, B1, F1, E1, E1, B0, E1, E1, F1, E1, Empty,
  E1, B1, A1, E1, F1, D1, D1, A1, G1, C1,
  B0, C1, D1, E1, F1, G1, A1, B1, A1, Eb,
  Empty
};

int noteDurations[] = {
  4, 4, 4,
  4, 4, 4,
  4, 4, 4,
  4, 4, 4,
  4, 4, 4,
  4, 4, 4,
  4, 4, 4,
  4, 4, 4,
  4, 4, 4, 
  4, 4, 4,
  4, 4, 4,
  12,
  4, 4, 4,
  4, 4, 4, 
  4, 4, 4,
  12, 900
    };

void setup() {
  pinMode(8, OUTPUT);
}

void loop() {
  for (int i = 0; i < sizeof(melody) / sizeof(melody[0]); i++) {
    int duration = 1000 / noteDurations[i];
    tone(8, melody[i], duration);
    delay(duration * 1.60);
    noTone(8);
  }
}