# 20221022
# Programmers_Lv0_머쓱이보다키큰사람

def solution(array, height):
    answer = 0
    
    for i in range(0, len(array)):
        if height < array[i]:
            answer += 1
    return answer