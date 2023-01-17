# 20220601
# Ch03_greedy_4_toOne.py

# 3-4. 1이 될 때까지
# 입력조건1. 첫째 줄에 N(2 <= N 100,000)과 K(2 <= N 100,000)가 공백으로 구분되며,
#           각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
# 출력조건1. 첫째 줄에 n이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.

# 예시 1)
# n, k를 공백으로 구분하여 입력받기
n, k = map(int(), input().split())

result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # n이 k로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
        n //= k 
        result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

# 예시 2)
# n, k를 공백으로 구분하여 입력받기
n, k = map(int(), input().split())

result = 0

while True:
    # (N==K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
       
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # k로 나누기
    result += 1
    n //= k
  
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
