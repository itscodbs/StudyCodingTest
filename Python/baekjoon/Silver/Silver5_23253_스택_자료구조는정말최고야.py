# 20230126
# Silver5_23253_스택_자료구조는정말최고야.py

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
sortBooks = True

for _ in range(m):
    input()    
    books = list(map(int, input().split()))
    
    if books != sorted(books, reverse=True):
        sortBooks = False
        break
        
if sortBooks:
    print('Yes')
else:
    print('No')
