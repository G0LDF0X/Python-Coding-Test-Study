import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 테스트 케이스의 개수 T (0 ≤ T ≤ 100)
T = int(input().strip())

def dfs(x, y):
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if grid_list[nx][ny] == "#" and visited[nx][ny] == 0:
            dfs(nx, ny)

for i in range(T):
    # H : 그리그의 높이 (0 < H ≤ 100)
    # W : 그리드의 너비 (0 < W ≤ 100)
    H, W = map(int, input().split())
    grid_list = []

    for j in range(H):
        grid = list(input().strip())
        grid_list.append(grid)

    visited = [[0] * W for _ in range(H)]
    count = 0

    for j in range(H):
        for k in range(W):
            if grid_list[j][k] == "#" and visited[j][k] == 0:
                dfs(j, k)
                count += 1

    print(count)
