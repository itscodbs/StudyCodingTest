# 20221006
# Baekjoon_Silver2_1260_DFSBFS_DFS와BFS

# 런타임 에러 방지
import sys
sys.setrecursionlimit(10 ** 6)

# stack 이용해서 dfs 구현
# 1. 현재 노드를 방문처리 한 후
# 2. 현재 노드와 연결되어 있는 노드들에 반복문 사용
# * 연결된 노드가 방문처리 되어있지 않은 노드라면 dfs() 함수 재귀적으로 사용
def DFS(num): # num : 방문한 노드
    print(num, end = ' ') # 처음 방문한 그 지점을 출력
    visited[num] = 1 # 방문했을 때 그 방문리스트에 0으로 되어있을 텐데, 그것을 1로 바꾸어준다.
    
    for i in range(N + 1):
        if visited[i] == 0 and ablist[num][i] == 1:
            DFS(i)

# queue를 이용해 bfs() 구현
# 1. 현재 노드를 방문처리 한 후
# 2. 현재 노드와 연결되어있는 노드들을 큐에 넣고 현재노드는 방문처리
# 3. pop()을 이용해 방문처리 되어있지 않은 노드라면 연결된 노드들을 다시 큐에 삽입.
#    큐가 비게 되면 반복문 종료
def BFS(num):
    result = [num]
    # 아까 DFS함수를 돌면서 visited리스트의 인덱스값을 모두 1로 바꾸어 주었던 상태이므로, 
    # 1인상태가 방문을 안한 상태이니까 방문을 했을 경우 0으로 바꾸어준다.
    visited[num] = 0 
    
    while(result):
        num = result[0]
        print(num, end = ' ')
        del result[0]

        for i in range(N + 1):
            if visited[i] == 1 and ablist[num][i] == 1:
                result.append(i)
                visited[i] = 0

import sys

N, M, V = map(int, sys.stdin.readline().split())
# N이 정점 개수, M이 간선 개수, V가 시작정점 이라고 생각하고 그래프를 그리는 것이라고 생각하고 코딩 시작.
# 간선 개수>
# 그래프를 컴퓨터가 이해하도록 설계하려면 matrix로 설계를 해야 컴퓨터가 이해를 합니다.
# matrix를 설계와 동시에 초기화까지 시켜줍니다.

ablist = [[0] * (N + 1) for _ in range(N + 1)]
#내가 방문한 점을 또 방문하면 안되니까 visited라는 1차원 행렬을 만들어줍니다.
visited = [0 for _ in range(N + 1)]

for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    ablist[a][b] = 1
    ablist[b][a] = 1

DFS(V)
print()
BFS(V)