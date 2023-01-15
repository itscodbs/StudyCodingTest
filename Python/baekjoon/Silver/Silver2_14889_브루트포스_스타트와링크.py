# 20221026
# Baekjoon_Silver2_14889_브루트포스_스타트와링크2

# 스타트팀과 링크팀의 능력치 차이 최솟값 구하기

import sys
from itertools import combinations

read = sys.stdin.readline
n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
result = int(1e9) # 최솟값을 추출할 결과값 변수에 정수 범위 설정

for team in combinations(range(0, n), n // 2):
    start = list(team)
    link = [i for i in range(0, n) if i not in start]

    s_score = l_score = 0

    for i in range(0, len(start) - 1):
        for j in range(i + 1, len(start)):
            s_score += graph[start[i]][start[j]] + graph[start[j]][start[i]]
            l_score += graph[link[i]][link[j]] + graph[link[j]][link[i]]

    result = min(result, abs(s_score - l_score)) # 능력치 차이 절대값의 최솟값 저장

print(result)

# 입력 1
# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0
# >> 0 

# 입력 2
# 6
# 0 1 2 3 4 5
# 1 0 2 3 4 5
# 1 2 0 3 4 5
# 1 2 3 0 4 5
# 1 2 3 4 0 5
# 1 2 3 4 5 0
# >> 2

# 입력 3
# 8
# 0 5 4 5 4 5 4 5
# 4 0 5 1 2 3 4 5
# 9 8 0 1 2 3 1 2
# 9 9 9 0 9 9 9 9
# 1 1 1 1 0 1 1 1
# 8 7 6 5 4 0 3 2
# 9 1 9 1 9 1 0 9
# 6 5 4 3 2 1 9 0
# >> 1