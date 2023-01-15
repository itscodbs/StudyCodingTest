 # 20221112
 # Programmers_Lv1_12919_서울에서김서방찾기

def solution(seoul):
    for index, name in enumerate(seoul):
        if name == 'Kim':
            answer = '김서방은 ' + str(index)+ '에 있다' 
            # index는 int형이므로 str 형태로 변환해주어야 함

            return answer

# 2) 
# def findKim(seoul):
#   return '김서방은 {}에 있다'.format(seoul.index('kim'))