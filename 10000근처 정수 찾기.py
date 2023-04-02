

#10000보다 큰 소수 10개, 작은 소수10개
#10000에서 작아지는 것  - while append된 리스트의 크기 size(X)<11
#10000에서 커지는 것  -
smallprime=[]
x=10000
while len(smallprime)<10 and x > 1 :
    Is_prime = True
    for i in range(2,x,1):
        if x % i == 0:
            Is_prime = False
            break
    if Is_prime :
        smallprime.append(x)
    x -= 1
print(smallprime)

y=10000
bigprime=[]
while len(bigprime)<10 and y > 1 :
    Is_prime = True
    for i in range(2,y,1):
        if y % i == 0:
            Is_prime = False
            break
    if Is_prime :
        bigprime.append(y)
    y+=1

print(bigprime)

import numpy as np
a=np.matrix(smallprime)
print(a)
b=np.matrix(bigprime).reshape(10,1)

print(a,b)
Result= np.dot(a,b)
print(Result)