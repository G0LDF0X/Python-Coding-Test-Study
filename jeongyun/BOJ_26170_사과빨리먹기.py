import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

        
graph = []
ans = 0
apple = 0

for i in range(5):
    arr = list(map(int, input().split()))
    graph.append(arr)
    
r, c = map(int, input().split())

q = deque([(r, c, 0)]) 

graph[r][c] = -1  
apple = 0

while q:
    x, y, dist = q.popleft()

    if apple == 3:
        print(dist)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if graph[nx][ny] == 1:
            apple += 1
            graph[nx][ny] = -1
            q.append((nx, ny, dist + 1))
            
            if apple == 3:
                dist +=1
                break
        elif graph[nx][ny] == 0:
            graph[nx][ny] = -1
            q.append((nx, ny, dist + 1))
        else:
            continue
        
if apple != 3:
    print(-1)
    
    
    