import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, H, W, location, visited):
    visited[x][y] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and location[nx][ny] == '#':
            dfs(nx, ny, H, W, location, visited)

T = int(input().strip())

for _ in range(T):
    H, W = map(int, input().split())
    location = [list(input().strip()) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    
    sheep_count = 0
    
    for i in range(H):
        for j in range(W):
            if location[i][j] == '#' and not visited[i][j]:
                dfs(i, j, H, W, location, visited)
                sheep_count += 1
    
    print(sheep_count)