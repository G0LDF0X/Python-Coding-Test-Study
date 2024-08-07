import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# R rows (1 ≤ R ≤ 100) -> 세로 길이
# C column (1 ≤ C ≤ 100) -> 가로 길이

R, C = map(int, input().split())
grass_list = []

for i in range(R):
    grass = list(input())
    grass_list.append(grass)

visited = [[0] * C for _ in range(R)]

def dfs(x, y):
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        
        if grass_list[nx][ny] == '#' and visited[nx][ny] == 0:
            dfs(nx, ny)

result = 0

for i in range(R):
    for j in range(C):
        if grass_list[i][j] == '#' and visited[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)