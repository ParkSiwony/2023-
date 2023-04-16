const int LED[] = {12, 11, 10, 9};  
const int N_L = sizeof(LED) / sizeof(LED[0]);  

void setup() {
  for (int i = 0; i < N_L; i++) {
    pinMode(LED[i], OUTPUT);  
  }
}

void loop() {
  // 왼쪽에서 오른쪽으로
  for (int i = 0; i < N_L; i++) {
    digitalWrite(LED[i], HIGH); 
    delay(121);  
  }
  for (int i = 0; i < N_L; i++) {
    digitalWrite(LED[i], LOW);  
    delay(100);  
  }

  // 오른쪽에서 왼쪽
  for (int i = N_L - 1; i >= 0; i--) {
    digitalWrite(LED[i], HIGH);  
    delay(144);  
  }
  for (int i = 0; i < N_L; i++) {
    digitalWrite(LED[i], LOW); 
    delay(100);  
  }
  // 왼쪽에서 오른쪽으로
  for (int i = 0; i < N_L; i++) {
    digitalWrite(LED[i], HIGH); 
    delay(121);  
  }
  for (int i = 0; i < N_L; i++) {
    digitalWrite(LED[i], LOW);  
    delay(100);  
  }

  // 오른쪽에서 왼쪽
  for (int i = N_L - 1; i >= 0; i--) {
    digitalWrite(LED[i], HIGH);  
    delay(144);  
  }
  for (int i = 0; i < N_L; i++) {
    digitalWrite(LED[i], LOW); 
    delay(100);  
  }

  // 왼쪽에서 오른쪽으로
  for (int i = 0; i < N_L; i++) {
    digitalWrite(LED[i], HIGH); 
    delay(121);  
  }
  for (int i = 0; i < N_L; i++) {
    digitalWrite(LED[i], LOW);  
    delay(100);  
  }

  // 오른쪽에서 왼쪽
  for (int i = N_L - 1; i >= 0; i--) {
    digitalWrite(LED[i], HIGH);  
    delay(144);  
  }
  for (int i = 0; i < N_L; i++) {
    digitalWrite(LED[i], LOW); 
    delay(100);  
  }


  //속도 느리게 
  for (int i = 0; i < N_L; i++) {
    digitalWrite(LED[i], HIGH);  
    delay(200); 
    digitalWrite(LED[i], LOW);  
    delay(200);  
  }

  // 랜덤으로
  for (int i = 0; i < 10; i++) {  
    int rand_L = random(N_L);  
    digitalWrite;
    digitalWrite(LED[rand_L], HIGH);  
    delay(100);  
    digitalWrite(LED[rand_L], LOW);  
    delay(100); 
  }
}
