# 20221026
# Baekjoon_Silver2_14889_브루트포스_스타트와링크

# DFS(백트래킹)

# 두 팀으로 나누기 위해 한 팀에 속하면 visited 리스트를 통해 방문처리 해주면서 재귀함수 형태로 만듦
# 만약, 한 팀에 속한 팀원의 명수가 n // 2 로 다 채워졌으면 스타트팀의 능력치와 링크팀의 능력치를 구함
# 방문처리된 팀이 스타트팀이라고 하면, 방문처리 안된 팀이 링크팀이다. 이것을 이용해서 능력치 구할 수 있음
# 스타트팀의 능력치와 스타트팀의 능력치의 차이의 절대값과 최소 능력치값을 비교하면서 계속 갱신해줌

import sys
read = sys.stdin.readline

n = int(input())

visited = [False for _ in range(n)] 
graph = [list(map(int, read().split())) for _ in range(n)]
result = int(1e9) # 결과값 출력 위해 result 값을 문제의 범위를 벗어나는 큰 수로 초기화

def dfs(depth, idx):
    global result # 최소 능력치값? 
    
    if depth == n // 2: # n // 2 번만큼 재귀를 돌면
        start = link = 0 # start팀과 link 팀 각각 0으로 선언

        # 이중리스트의 열은 굳이 0부터 돌 필요가 없기 때문에 i+1 로 범위를 좁혀준다
        # 만약, i,j 둘 다 방문했다면 방문한 사람을 스타트팀에 더해준다
        # 방문하지 않은 i,j는 링크팀이므로 방문 안한 사람을 링크팀에 더해준다
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        
        result = min(result, abs(start - link)) # 최솟값을 결과값에 대입
        return

    # 만약, 방문을 안했다면 방문 처리, 재귀 반복, 방문 완료 처리
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(result)