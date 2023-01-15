 # 20221112
 # Programmers_Lv1_12969_직사각형별찍기

a, b = map(int, input().strip().split(' '))

for i in range(b): # 열
    for j in range(a): # 행
        print('*', end = '')
    print()