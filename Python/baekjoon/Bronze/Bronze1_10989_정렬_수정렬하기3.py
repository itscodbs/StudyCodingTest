# 20230123
# Bronze1_10989_정렬_수정렬하기3.py

n = int(input())
m = [int(input()) for _ in range(n)]
m.sort()

for i in range(n):
    print(m[i])

# 입력
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7

# 출력
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7
