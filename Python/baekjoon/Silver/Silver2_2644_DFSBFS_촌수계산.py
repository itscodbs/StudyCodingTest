# 20221016
# Baekjoon_Silver2_2644_DFSBFS_촌수계산
# 메모리 : 30840kb, 시간 : 68ms

import sys
read = sys.stdin.readline

# 전체 인원 n 
n = int(input())

# 촌수를 계산해야 하는 서로 다른 두 사람의 번호 b1, b2
c1, c2 = map(int, read().split())

# 부모 자식들 간의 관계의 개수 m
m = int(input())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)
cnt = 0

# 부모 자식간의 관계를 나타내는 번호 x, y
for i in range(m):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x)

# bfs 정의
def bfs(n, e):
    global cnt
    visited[n] = True

    if c2 == n:
        cnt = e
        return
    
    answer[n] = e
    for i in graph[n]:
        if not visited[i]:
            bfs(i, e + 1)

bfs(c1, 0)

if visited[c1] and visited[c2]:
    print(cnt)
else:
    print(-1)