import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs_iterative(start_x, start_y):
    stack = [(start_x, start_y)]
    visited[start_x][start_y] = True
    
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
    
    
t = int(input())
for i in range(t):
    h, w = map(int, input().split())
    graph = []
    visited = [[False]*w for _ in range(h) ] 
    for j in range(h):
        arr = list(input().strip())     # 각 문자를 리스트로 변환
        graph.append(arr)
    # print(graph)
    
    ans = 0
    for l in range(h):
        for m in range(w):
            if graph[l][m] == '#' and not visited[l][m]:
                dfs_iterative(l, m)
                ans +=1
    print(ans)
    
    
    
# import sys
# from collections import deque

# input = sys.stdin.readline

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dfs(x, y):
    
#     visited[x][y] = True
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if 0 <= nx < h and 0 <= ny < w:
#             if graph[nx][ny] == '#' and not visited[nx][ny]:
#                 dfs(nx, ny)
    
    
# t = int(input())
# for i in range(t):
#     h, w = map(int, input().split())
#     graph = []
#     visited = [[False]*w for _ in range(h) ] 
#     for j in range(h):
#         arr = list(input().strip())     # 각 문자를 리스트로 변환
#         graph.append(arr)
#     # print(graph)
    
#     ans = 0
#     for l in range(h):
#         for m in range(w):
#             if graph[l][m] == '#' and not visited[l][m]:
#                 dfs(l, m)
#                 ans +=1
#     print(ans)
    
    