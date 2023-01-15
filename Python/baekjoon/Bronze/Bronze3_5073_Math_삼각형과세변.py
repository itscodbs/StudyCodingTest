# 2022
# Baekjoon_Bronze3_5073_Math_삼각형과세변

while True :
    data = list(map(int, input().split()))

    if data[0] == 0 and data[1] == 0 and data[2] == 0 :
        break
        
    data.sort(reverse=True)
    
    if data[0] >= data[1] + data[2] :
        print("Invalid")
    elif data[0] == data[1] == data[2] :
        print("Equilateral")
    elif data[0] == data[1] or data[0] == data[2] or data[1] == data[2] :
        print("Isosceles")
    else :
        print("Scalene")