# 20230127
# Bronze2_17608_스택_막대기.py

import sys

read = sys.stdin.readline
n = int(read())
# sticks = [int(read()) for _ in range(n)]
sticks = list(map(int, read().split()))
cnt, maxStick = 0, 0

for i in reversed(sticks):
    if maxStick < i:
        maxStick = i
        cnt += 1
    
print(cnt)
