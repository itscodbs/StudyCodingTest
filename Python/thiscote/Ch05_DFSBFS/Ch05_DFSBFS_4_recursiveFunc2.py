# 20220620
# Ch05_DFSBFS_4_recursiveFunc2.py

def recursive_Function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return

    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_Function(i + 1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_Function(1)
