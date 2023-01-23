# 20230121
# Baekjoon_Silver3_16967_배열_배열복원하기.py
# 배열 B의 (i, j)에 들어있는 값은 아래 3개 중 하나이다.
# (i, j)가 두 배열 모두에 포함되지 않으면, B[i][j] = 0이다.
# (i, j)가 두 배열 모두에 포함되면, B[i][j] = A[i][j] + A[i-X][j-Y]이다.
# (i, j)가 두 배열 중 하나에 포함되면, B[i][j] = A[i][j] 또는 A[i-X][j-Y]이다.
# TypeError: 'int' object is not subscriptable는 인덱스를 갖지않는 값에
#            인덱스를 가지게 코드를 짤 경우 발생하는 오류이다.

import sys

read = sys.stdin.readline
H, W, X, Y = map(int, read().split())
arrs = [list(map(int, read().split())) for _ in range(H + X)]

for i in range(H - X):
    for j in range(W - Y):
        arrs[i + X][j + Y] -= arrs[i][j]

for k in range(H):
    print(*arrs[k][0:W])

# import sys
# read = sys.stdin.readline

# # 첫째줄에 정수 4개 입력받기
# H, W, X, Y = map(int, read().split())

# # 배열 A, B 선언
# graphA = [[0] * W for _ in range(H)]
# graphB = [list(map(int, read().split())) for _ in range(H+X)]

# # 안 겹치는 부분 
# for i in range(H):
#     for j in range(W):
#         graphA[i][j] = graphB[i][j]

# # 겹치는 부분 
# for i in range(X, H):
#     for j in range(Y, W):
#         graphA[i][j] = graphB[i][j] - graphA[i-X][j-Y]

# for i in range(H):
#     for j in range(W):
#         print(graphA[i][j], end=" ")
#     print()

# 입력
# 2 4 1 1
# 1 2 3 4 0
# 5 7 9 11 4
# 0 5 6 7 8

# 출력
# 1 2 3 4
# 5 6 7 8

# 시행착오
# H, W, X, Y = list(map(int, input().split()))
# HX = H + X
# WY = W + Y
# graphA, graphB = [], []

# for i in range(HX):
#     # for j in range(WY):
#     graphB = list(map(int,input().split())) 

# for i in range(HX):
#     for j in range(WY):
#         if i < X and j < Y: # 윗쪽 안 겹치는 부분
#             graphA[i][j] = graphB[i][j]
#         elif j < Y and i < H: # 왼쪽 안겹치는 부분
#             graphA[i][j] = graphB[i][j]
#         elif i < H and j < W and i >= X and j >= Y: # 겹치는 부분 
#             graphA[i][j] = graphB[i][j] or graphA[i-X][j-Y]

# # 배열A 출력
# for i in range(H):
#     for j in range(W):
#         print(graphA[i][j], end='')
#     print()
