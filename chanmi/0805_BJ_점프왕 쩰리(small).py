import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 게임 구역의 크기 N (2 ≤ N ≤ 3)
N = int(input().strip())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

visited = [[0] * N for _ in range(N)]

def dfs(x, y):
    visited[x][y] = 1

    dx = [graph[x][y], 0]
    dy = [0, graph[x][y]]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if visited[nx][ny] == 0:
            dfs(nx, ny)

dfs(0, 0)

if visited[N - 1][N - 1] == 1:
    print("HaruHaru")
else:
    print("Hing")