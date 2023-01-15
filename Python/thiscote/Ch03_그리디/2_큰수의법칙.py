# 20220527
# Ch03_그리디_2_큰수의법칙

# 예시1)
n, m, k = map(int, input().split()) # 5, 8, 3

# n개의 수를 공백으로 구분하여 입력받기 (list 형태로)
data = list(map(int, input().split())) # 2 4 5 4 6

data.sort() #입력받은 수 정렬 : 24456
first = data[n - 1] # 가장 큰 수 6. n 크기가 5이므로 인덱스 마지막인 n-1 
second = data[n - 2] # 두번째로 큰 수 5
result = 0

while True:
    for i in range(k): # 가장 큰 수 first를 k=3번 더하기
        if m == 0: # m=8이 0이 되면 반복문 탈출 -> 8번 반복
            break

        result += first
        m -= 1 # 더할 때마다 1씩 빼기. 8,7,6,5,4,3,2,1
    
    if m == 0: # m=8이 0이 되면 반복문 탈출
        break
    result += second # 두번째로 큰 수 1번 더하기. 가장 큰 수 만들기 위해
    m -= 1

print(result)

# 예시2)

# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
cnt = int(m / (k + 1)) * k
cnt += m % (k + 1)

result = 0
result += (cnt) * first # 가장 큰 수 더하기
result += (m - cnt) * second # 두번째로 큰 수 더하기

print(result)