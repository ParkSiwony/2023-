import numpy as np
import pandas as pd

def compare(x):  # x에 들어갈 것은 반복 횟수
    Final_count = []
    for i in range(0, x, 1):
        Same_count = []
        RN = np.random.randint(10, size=1000000)
        for j in range(0, 1000000 - 5):  # 뒤에서 6번째 까지만
            if np.array_equal(RN[j:j + 6], np.array([3, 4, 0, 0, 2, 7])):  # np array 비교
                Same_count.append(1)
        Final_count.append(len(Same_count))
    Expected_value = int(sum(Final_count))
    Result = Expected_value/x
    return Result

print(compare(100))

#이론적인 개수
n=999995
p=0.1**6
print(n*p)
