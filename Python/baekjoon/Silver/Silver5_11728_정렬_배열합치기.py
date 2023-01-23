# 20230120
# Baekjoon_Silver5_11728_정렬_배열합치기.py

# 정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

n, m = list(map(int, input().split()))
n1 = list(map(int, input().split()))
m1 = list(map(int, input().split()))

s = n1 + m1
s.sort()
print(*s)

# 입력
# 2 2
# 3 5
# 2 9

# 출력
# 2 3 5 9

# 중복체크 in list면 continue
