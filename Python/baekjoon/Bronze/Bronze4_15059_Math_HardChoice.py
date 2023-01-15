# 2022
# Baekjoon_Bronze4_15059_Math_HardChoice

# 닭고기, 소고기, 파스타 총 식사 수 입력받기
c, b, p = map(int, input().split())

# 요청 받은 식사 수 입력받기
c2, b2, p2 = map(int, input().split())

sum = max(0, c2 - c) + max(0, b2 - b) + max(0, p2 - p) 
   
print(sum)