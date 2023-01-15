graph = []

for i in range(12):
  graph.append([])
  for j in range(12):
    graph[i].append(0)

for i in range(10):
  a = input().split()
  for j in range(10):
    graph[i + 1][j + 1] = int(a[j])

x = 2
y = 2

while True:
  if graph[x][y] == 0:
    graph[x][y] = 9
  elif graph[x][y] == 2:
    graph[x][y] = 9
    break
  
  if(graph[x][y + 1] == 1 and graph[x + 1][y] == 1) or (x == 9 and y == 9):
    break
  
  if graph[x][y + 1] != 1:
    y += 1
  elif graph[x + 1][y] != 1:
    x += 1
    
for i in range(1, 11):
  for j in range(1, 11):  
    print(graph[i][j], end=' ')
  print()