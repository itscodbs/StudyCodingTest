# 20221026
# Baekjoon_Gold4_14502_Implement,BFS_연구소

# 1. 벽세우기 (입력값에 n과 m이 작은 것을 보고 브루트포스 방법 사용)
# 2. 바이러스 감염 (dfs or bfs 둘 중 하나로 구현)
# 3. 안전 영역 구하기

# 1) 지도에서 빈 공간들의 좌표 저장
# 2) combinations 사용하여 벽이 세워지는 모든 경우의 수 추출
# 3) deepcopy 사용해 2차원 리스트 복사해오고 빈 공간 3곳에 벽 세우기
# 4) 각 바이러스 위치에 대해 infection() dfs 함수로 바이러스 감염 실행

import sys
import copy
from itertools import combinations

input = sys.stdin.readline # 빠른 결과값 출력 
sys.setrecursionlimit(10 ** 6)

blank = [] # 빈공간 리스트
mapp = [] # 지도
virus = [] # 바이러스 위치 리스트
resultList = []

# 입력
n, m = map(int, input().split())

for i in range(n):
    mapp.append([int(x) for x in input().split()])
    for j in range(m):
        if mapp[i][j] == 2:  # 바이러스 위치 저장
            virus.append([i, j])
        elif mapp[i][j] == 0:  # 빈공간, 벽이 들어 갈 수 있는 위치 저장
            blank.append([i,j])

# 바이러스 감염
# 좌표의 경계값이 넘어가거나 벽이 있는 경우 : return False 해주고
# 빈 공간(0)이거나 바이러스(2)가 있는 경우 : 감염을 3으로 표시.
# 이후 상하좌우 dfs 방법으로 탐색

def infection(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if bList[x][y] == 1:
        return False

    if bList[x][y] == 0 or bList[x][y] == 2:
        bList[x][y] = 3 # 바이러스 감염 3
        infection(x - 1, y)
        infection(x + 1, y)
        infection(x, y - 1)
        infection(x, y + 1)
        return True
    return False

# bList (리스트 b)에 빈 공간(0)의 개수를 세고, 
# 결과값을 모아주는 resultList(결과리스트)에 추가
# resultList에서 최대결과값 출력
for a in combinations(blank, 3):
    bList = copy.deepcopy(mapp)

    for s in a:
        p = s[0]
        q = s[1]
        bList[p][q] = 1  # 벽 세우기

    for v in virus:
        infection(v[0], v[1])

    result = 0

    for i in range(n):
        result += bList[i].count(0)
    resultList.append(result)

print(max(resultList))