# 20221022
# Programmers_Lv0_짝수의합

def solution(n):
    answer = 0
    for i in range(n+1): # 범위 설정
        if i % 2 == 0:
            answer += i
    return answer