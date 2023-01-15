# 2022
# CodeUp_6097_설탕과자 뽑기

# w, h (가로, 세로) 공백으로 입력받기
b = []
w, h = map(int, input().split())

# w, h 크기만큼 b에 2차원 리스트 만들어주기
for i in range(w): 
  b.append([])  
  for j in range(h): 
    b[i].append(0)

# 놓을 수 있는 막대의 개수 n 입력받기
n = int(input())

# 각 막대의 길이 m, 방향 d, 좌표 x, y 입력받기
# m = 막대의 길이만큼 1로 채우기
# d = 0 : 가로, d = 1 : 세로
# x, y = 막대가 시작되는 좌표
for i in range(n):
  m, d, x, y = map(int, input().split())

  for j in range(m):
    # d가 0이면 가로로 진행, d가 1이면 세로로 진행    
    if d == 0: 
      b[x-1][y-1] = 1     
      y += 1
    else:
      b[x-1][y-1] = 1
      x += 1
  
# 막대가 놓인 격자판 출력
for i in range(w):
  for j in range(h): 
    print(b[i][j], end=' ')
  print()