import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 8방향 설정: 상하좌우 및 대각선 방향
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = []
    visited = [[False] * w for _ in range(h)]
    ans = 0
    
    for i in range(h):
        arr = list(map(int, input().split()))
        graph.append(arr)
        
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                ans += 1
                
    print(ans)
