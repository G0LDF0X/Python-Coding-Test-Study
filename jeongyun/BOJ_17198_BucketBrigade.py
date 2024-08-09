import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[start_x][start_y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
        if 0 <= nx < 10 and 0<= ny < 10 :
            if visited[nx][ny] == 0 and graph[nx][ny] != 'R':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            if graph[nx][ny] == 'B':
                return visited[nx][ny]-1
    
    return -1

# 그래프 초기화 
graph = []
for i in range(10):
    arr = list(input().strip())
    graph.append(arr)
    
visited = [[0] * 10 for _ in range(10)]
# B, L 의 좌표 찾기 
for i in range(10):
    for j in range(10):
        if graph[i][j] == 'L':
            start_x = i
            start_y = j
                
print(start_x, start_y)
ans = bfs(start_x, start_y)
print(ans)
# L 에서 B 까지 최소 경로 (R은 가지 못함.)
# L 에서 시작해서 BFS / .의 갯수 count 
