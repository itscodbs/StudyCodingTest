# 2022
# CodeUp_6098_성실한개미

# 미로 상자 넣을 graph 변수
graph = []

# 10x10 크기로 미로 상자의 구조와 먹이의 위치 입력받기
for i in range(12):
  graph.append([])
  for j in range(12):
    graph[i].append(0)

# 10x10 크기의 미로상자에 0,1로 미로 만들기 
for i in range(10):
  a = input().split()
  for j in range(10):
    graph[i + 1][j + 1] = int(a[j])

# 0 : 갈 수 있는 곳, 1 : 벽 또는 장애물, 2 : 먹이. 최종 도착지점
# 방향 설정 : dr = 오른쪽, dd = 아래쪽

# 개미집이 (2,2)에 존재하므로 (2,2)부터 시작점 설정
# graph[2][2] = 9 
x = 2
y = 2

# 방문 프로세스
while True:
  # 0이면 9로 처리. 2면 9로 처리 후 종료.
  if graph[x][y] == 0:
    graph[x][y] = 9
  elif graph[x][y] == 2:
    graph[x][y] = 9
    break
  
  # 오른쪽이나 아래쪽으로 갔을 때 1이거나 방문한 곳이면 종료
  if(graph[x][y + 1] == 1 and graph[x + 1][y] == 1) or (x == 9 and y == 9):
    break
  
  # 오른쪽이나 아래쪽으로 갔을 때 1이 아니면 계속 이동
  if graph[x][y + 1] != 1:
    y += 1
  elif graph[x + 1][y] != 1:
    x += 1
    
# 개미굴 출력
for i in range(1, 11):
  for j in range(1, 11):  
    print(graph[i][j], end=' ')
  print()