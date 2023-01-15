# 22020604
# Ch04_구현_1_상,하,좌,우

# n 입력받기
n = int(input()) # 5
x, y = 1, 1 # 가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (n, n)
plans = input().split() # R R R U D D

# 좌, 우, 상, 하에 따른 이동 방향. 공간 밖 영역은 무시
dx = [0, 0, -1, 1] # 상,하
dy = [-1, 1, 0, 0] # 좌,우
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):  # 4?
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 이동 수행
    x, y = nx, ny

print(x, y)
print("여행가 A의 현재 위치는 (", x, ",", y, ") 입니다.")

# 입력예시
# 5
# R R R U D D
# 출력예시
# 3 4
# 여행가 A의 현재 위치는 ( 3 , 4 ) 입니다.