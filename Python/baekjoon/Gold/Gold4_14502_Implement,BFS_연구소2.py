# 20221026
# Baekjoon_Gold4_14502_Implement,BFS_연구소

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

brr = []
zero = []
two = []
max_ = 0

dr = [-1, 0, 1, 0] # 행 상 우 하 좌
dc = [0, 1, 0, -1] # 열 상 우 하 좌

# 0과 2의 위치 찾기
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            zero.append((i, j))
        elif graph[i][j] == 2:
            two.append((i, j))

# 바이러스가 퍼지는 위치를 확인하여 안전지대 개수 구하기
def bfs(dump_map):
    global max_

    visited = [[False] * m for _ in range(n)]
    queue = deque() # deque() 함수 저장해주기

    for i in range(len(two)):
        queue.append(two[i])

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >- m or visited[nr][nc] or dump_map[nr][nc]:
                continue

            dump_map[nr][nc] = 2
            visited[nr][nc] = True
            queue.append((nr, nc))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if not dump_map[i][j]:
                cnt += 1
    
    if max_ < cnt:
        max_ = cnt

# 0의 위치에서 3개를 뽑은 후 벽으로 바꾸어준다.
def dfs(cur, start):
    if cur == 3:
        dump_map = []

        for i in range(n):
            dump_map.append(graph[i][:])

        for r, c in brr:
            dump_map[r][c] = 1
        
        bfs(dump_map)
        return

    for i in range(start, len(zero)):
        brr.append(zero[i])
        dfs(cur + 1, i + 1)
        brr.pop()

dfs(0, 0)
print(max_)