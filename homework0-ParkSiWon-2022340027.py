#나머지(첫 번째 매개 변수를 두 번째 매개 변수로 나눈 후 남은 값)
class Calculator:  #class 클래스이름:
    def __init__(self, num1, num2): # 생성자 def __init__(self, name):
        self.num1 = num1
        self.num2 = num2

    def sum(self):                  #def 메서드이름(self):
        result = self.num1 + self.num2
        return result
    def sub(self):
        result = self.num1 - self.num2
        return result
    def mul(self):
        result = self.num1 * self.num2
        return result
    def div(self):
        result = self.num1 // self.num2
        remainder = self.num1 % self.num2
        return result, remainder
        Value = list(result, remainder)

def Function(a,b,B):
      if str(B) == '+':
          Function = Calculator(a, b)
          print(Function.sum())
      elif str(B) == '-':
          Function = Calculator(a, b)
          print(Function.sub())
      elif str(B) == '*':
          Function = Calculator(a, b)
          print(Function.mul())
      elif str(B) == '/':
          Function = Calculator(a, b)
          print(Function.div())

Function(34,5,'/')  #함수 안에 사칙연산부호를 str자료형 외에
# 어떻게 + 나 - 로 바로 집어 넣을 수 있는 지 모르겠습니다.

print(type(str('+')))
