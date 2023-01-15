# 20221030
# Silver1_2178_DFSBFS_미로탐색
# 이코테 dfsbfs escape와 소스코드 동일 

# n, m 크기의 배열로 표현되는 미로
# 1 : 이동가능, 0 : 이동불가
# (1, 1)에서 출발하여 (n, m)의 위치로 이동할 때 지나야하는 최소의 칸 수

from collections import deque
import sys

read = sys.stdin.readline
graph = []
n, m = map(int, input().split())

# 0과 1의 그래프 만들기
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 상, 하, 좌, 우 방향 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색
def bfs(x, y):
    # deque 라이브러리 사용하여 큐 구현
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가 (미로 찾기 공간을 벗어난 경우 무시)
            # 0 < nx, ny <= n, m
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽이므로 진행 불가
            if graph[nx][ny] == 0:
                continue

            # 벽이 아니므로 이동
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m -1]

# bfs 수행 결과 출력
print(bfs(0, 0))