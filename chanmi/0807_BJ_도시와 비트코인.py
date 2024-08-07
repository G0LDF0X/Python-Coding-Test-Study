import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 도시는 가로 N, 세로 M 크기의 격자 모양
# 진우는 북서쪽 끝(0, 0)에 있고, 거래소는 남동쪽 끝(N-1, M-1)에 있음
# 오른쪽 아니면 아래로만 이동 가능
# 거래소로 갈 수 있는지 여부 출력

# N : 가로 크기 (1 ≤ N ≤ 300)
# M : 세로 크기 (1 ≤ M ≤ 300)
N, M = map(int, input().split())
city_list = []

for i in range(M):
    city = list(map(int, input().split()))
    city_list.append(city)

# 1 : 진우가 갈 수 있는 칸
# 0 : 진우가 갈 수 없는 칸

visited = [[0] * N for _ in range(M)]

def dfs(x, y):
    visited[x][y] = 1

    dx = [1, 0]
    dy = [0, 1]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue

        if city_list[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

dfs(0, 0)

if visited[M-1][N-1] == 1:
    print("Yes")
else:
    print("No")