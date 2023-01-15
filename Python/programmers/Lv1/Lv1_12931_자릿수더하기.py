# 20221112
# Programmers_Lv1_12931_자릿수더하기

def solution(n):
    answer = 0
    n = str(n) # 123
    
    # 전달받은 정수형 n을 문자열 형태로 변환하고, 각 자릿수를 정수형으로 변환하여 answer에 더한다.
    for value in n: # n의 길이만큼 반복
         answer += int(value)

    return answer