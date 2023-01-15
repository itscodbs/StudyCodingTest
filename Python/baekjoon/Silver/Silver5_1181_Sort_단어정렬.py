# 2022
# Baekjoon_Silver5_1181_Sort_단어정렬

import sys

# 단어의 개수 n 입력받기.
n = int(sys.stdin.readline())

arr = []

for i in range(n):
    arr.append(sys.stdin.readline().strip())

arr = list(set(arr))
arr.sort()
arr.sort(key = len)

for i in arr:
    print(i)