# 20230121
# Bronze1_2693_정렬_N번째큰수.py
# 배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.
# 배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

n = int(input()) 

for i in range(n):
    a = list(map(int, input().split()))
    a.sort()
    print(a[-3])

# 입력
# 1 2 3 4 5 6 7 8 9 1000
# 338 304 619 95 343 496 489 116 98 127
# 931 240 986 894 826 640 965 833 136 138
# 940 955 364 188 133 254 501 122 768 408
# 출력
# 8
# 489
# 931
# 768

# arr = int(input()) 
# n = 3
# graphA = []

# for i in range(arr):
#     a = list(map(int, input().split()))
#     graphA.append(a)

# for j in range(arr):
#     graphA[j].sort(reverse=True)

# for k in range(arr):
#     print(graphA[k][2])
