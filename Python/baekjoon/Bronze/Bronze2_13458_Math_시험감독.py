# 2022
# Baekjoon_Bronze2_13458_Math_시험감독

# 시험장 개수 n 입력받기
room = int(input())

# 각 시험장의 응시자 수 a 입력받기
student = map(int, input().split())

# 총감독관, 부감독관이 감시할 응시자 수 a, b 각각 입력받기
# 총감독관은 1명만 있어야 하고, 부감독관은 여러 명 있어도 됨
a, b = map(int, input().split())

# 각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수 출력
cnt = room

for i in student:
    i -= a
    if i > 0:
        if i % b:
            cnt += (i // b) + 1
        else:
            cnt += (i // b)

print(cnt)