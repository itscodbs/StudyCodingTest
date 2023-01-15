# 20221022
# Programmers_Lv0_자릿수더하기

def solution(n):
    answer = 0
    n = list(map(int, str(n))) # list로 변환
    
    for i in range(len(n)): # 리스트 크기
        answer += n[i]
    return answer