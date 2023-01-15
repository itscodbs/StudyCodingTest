# 20221022
# Programmers_Lv2_최댓값과최솟값

def solution(s):
    answer = ''
    s = list(map(int, s.split())) # 리스트로 쪼개기
    s.sort()
    answer = "" + str(min(s)) + ' ' + str(max(s)) + "" # 따옴표 사용주의
    return answer