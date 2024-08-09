import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))


m, n = map(int, input().split())
graph = []
visited = [[False]*n for _ in range(m)]

for i in range(m):
    arr = list(map(int, input().strip()))
    graph.append(arr)
    
# print(graph)

for i in range(n):
    if graph[0][i] == 0 and not visited[0][i]:
        dfs(0, i)
if True in visited[m-1]:
    print('YES')
else:
    print('NO')
