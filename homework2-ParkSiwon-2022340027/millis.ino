#include <Arduino.h>
#include <TM1637Display.h> // TM1637Display 라이브러리를 불러옵니다.


const int CLK = 9;  .
const int DIO = 8;  

TM1637Display display(CLK, DIO);

void setup()
{
  display.setBrightness(0x0f);  //밝기 최대
}

void loop()
{
  int minutes = 0;
  int seconds = 0;
  unsigned long Start = millis();  //unsigned long millis함수자료형
  
  while (minutes < 10) {  
    display.showNumberDecEx(minutes * 100 + seconds, 0b01000000, true);  //minutes 3번째 자리+초1,2번째,소수점,10초보다 작으면 앞에 0 
    delay(1000); 
    seconds++;  //분,초 타이머 만드는 법
    if (seconds == 60) {  
      minutes++;
      seconds = 0;
    }
  }
  
  unsigned long Finish = millis();  // 끝 시간
  unsigned long Differnce = Finish - Start;  // 시간 오차
  display.showNumberDecEx(Differnce, 0b01000000, true);  //오차 표시
  while (true) {}  //끝내기 무한 루프
}
