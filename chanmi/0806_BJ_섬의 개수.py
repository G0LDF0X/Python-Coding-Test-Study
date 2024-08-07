import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 지도의 너비 w (1 ≤ w ≤ 50)
# 지도의 높이 h (1 ≤ h ≤ 50)

def dfs(x, y):
    visited[x][y] = 1

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue

        if land_list[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    land_list = []
    for i in range(h):
        land = list(map(int, input().split()))
        land_list.append(land)

    visited = [[0] * w for _ in range(h)]
    island_count = 0
    for i in range(h):
        for j in range(w):
            if land_list[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                island_count += 1

    print(island_count)