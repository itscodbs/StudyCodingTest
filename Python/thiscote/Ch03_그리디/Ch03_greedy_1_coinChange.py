# 20220527
# Ch03_greedy_1_coinChange.py

n = 1260
cnt = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types: # coin : 500, 100, 50, 10
    cnt += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
    n %= coin

print(cnt)

# 몫만 cnt 변수에 누적합 해주면 됨.
# 누적합 해주려면 n 변수 금액을 나머지 금액으로 저장해서 계산.
# for문 사용

# n=1260 // coin=500 -> cnt=2개, n=260
# n=260 // coin=100 = cnt=2개, n=60
# n=60 // coin=50 = cnt=1개, n=10
# n=10 // coin=0 = cnt=1개, n=0

# 1) cnt=0 += n=1260 // coin=500 : cnt=2
#    n=1260 %= coin=500 : n=260 나머지를 n으로 저장.
# 2) cnt=2 += n=260 // coin=100 : cnt=2
#    n=260 %= 100 : n=60
# .....
