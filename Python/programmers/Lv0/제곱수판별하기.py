# 20221022
# Programmers_Lv0_제곱수판별하기

def solution(n):
    answer = 0
    if n == int(n**(1/2))**2:
        answer = 1
    else:
        answer = 2
    return answer

 # import 사용   
import math

def solution(n):
    answer = 0
    if n == int(math.sqrt(n))**2:
        answer = 1
    else:
        answer = 2
    return answer