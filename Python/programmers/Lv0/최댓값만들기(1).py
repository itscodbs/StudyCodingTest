# 20221022
# Programmers_Lv0_최댓값만들기(1)

def solution(numbers):
    answer = 0
    # numbers = sorted(numbers, reverse = True)
    numbers.sort(reverse=True)
    max1 = numbers[0] # 괄호사용 주의
    max2 = numbers[1]
    answer = max1 * max2

    return answer