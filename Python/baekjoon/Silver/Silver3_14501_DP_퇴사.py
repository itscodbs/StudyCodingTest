# 2022
# Baekjoon_Silver3_14501_DynamicPrgramming_퇴사

n = int(input())

t_list = []
p_list = []
opt = [0] * (n + 1) # 최적해를 저장할 변수 format

for i in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

for i in range(n - 1, -1, -1):
    if t_list[i] + i > n:
        opt[i] = opt[i + 1]
    else:
        opt[i] = max(p_list[i] + opt[i + t_list[i]], opt[i + 1])

print(opt[0])