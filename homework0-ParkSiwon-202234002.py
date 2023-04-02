#HW0-(1)
#나머지(첫 번째 매개 변수를 두 번째 매개 변수로 나눈 후 남은 값)
import random


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

Function(34,5,'/')  #함수 안에 사칙연산부호(내장함수취급?)를 str자료형 외에
# 어떻게 + 나 - 로 바로 집어 넣을 수 있는 지 모르겠습니다.

print(type(str('+')))






#HW0-(2)
#
# a.append([]) 활용해서 최종 리스트에 집어 넣기
# 반복하기
# nympy 사용해서 10x10 행렬 만들기
print(random.randrange(0,9))
import numpy as np
import pandas as pd  #panda의 series 자료형 = 값 Value + 이름 Index

a = np.random.randint(10, size=100).reshape(10,10)
print(type(a)) #a의 자료형이 궁금해서 해봄
print(a)

# nd.array(10x10)은 2차원이라서 series 자료형으로 변경이 불가능하다고 해서
# 1차원 변수인 b를 만들어서 Series 자료형화 해봄
b=pd.Series(np.random.randint(10, size=100))
print("""b행렬의 Series 자료형입니다. - 과제 아님""",b, sep="\n")


a = np.ravel(a, order='c') # 다차원 행렬을 일차원 행렬로 바꾸는 메서드가 numpy에 있다는 것을 알게됨
a=pd.Series(a)
print("""a행렬의 Series 자료형입니다.""", a, sep="\n")

num0 = a.value_counts() #각 value가 몇번씩 나왔는지 series자료형으로 표현
print(num0)

import matplotlib.pyplot as plt
num0_index=list(num0.index)
num0_values=list(num0.values)
plt.bar(num0_index,num0_values)
plt.xticks(range(0,10,1))
plt.show()





#HW0-(3)
#  List[0],List[3]=List[3],List[0]
ri=list(np.random.randint(10000, size=1000)) #1000개의 정수 난수 형성 10000미만 정수로 하기로 함
print(ri)
def find(x):                    # 반복(리스트안에 K+1번째 순서 이상의 리스트 안 가장 작은 값을 찾기- 함수?)
    for k in range(len(x)):    #리스트 안에 k번째  0~9
        for j in range(len(x)-k): # 반복 min함수를 for문으로 대신 이용  0~9-k
            if x[k] >= x[k+j]:
                x[k],x[k+j]=x[k+j],x[k]
            else:
                x[k],x[k+j]=x[k],x[k+j]
    return x
print(find(ri))

