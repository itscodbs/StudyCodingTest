# 20220711
# Ch08_dynamicPrgm_3_funcCheck.py

d = [0] * 100

def fibo(x):
    print('f(' + str(x) + ')', end = ' ')

    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x -1) + fibo(x - 2)
    return d[x]

fibo(6) # 결과값 f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4) 
