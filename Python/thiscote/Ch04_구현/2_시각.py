# 22020604
# Ch04_구현_2_시각

# h를 입력받기
h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# 5 = 5시간
# 11475 = '3' 이 포함된 모든 경우의 수