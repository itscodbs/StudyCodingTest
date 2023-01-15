# 20221022
# Programmers_Lv1_완전탐색_모의고사

def solution(answers):
    # 수포자들의 데이터를 list 형태로 저장
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []
    
    # 반복문으로 answer 값과 수포자들이 찍은 값을 비교 후,
    # 각 사람의 점수를 score에 저장
    # enumerate() : 인덱스 요소들 열거
    for i, answer in enumerate(answers):
        if answer == pattern1[i%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[i%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[i%len(pattern3)]:
            score[2] += 1
            
    # score에서 가장 큰 값과 다른 모든 값을 비교해 일치할 경우,
    # 해당 인덱스에 +1 한 값을 result에 넣음(app end)
    for i, s in enumerate(score):
        if s == max(score):
            result.append(i + 1)
            
    return result