# 2022
# Baekjoon_Bronze3_23971_Math_ZOAC4

import math

H, W, N, M = list(map(int, input().split()))

# math.ceil() 함수는 올림 기능
a = math.ceil(H/(N+1)) # 세로에 몇명이 앉는지 계산
b = math.ceil(W/(M+1)) # 가로에 몇명이 앉는지 계산

result = a * b

print(result)