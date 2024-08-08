import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 격자는 M*N 사이즈
# 격자 위쪽을 바깥쪽(outer side)
# 격자 아래쪽을 안쪽(inner side)

# 검은색 격자 : 전류 차단
# 흰 색 격자 : 전류 통함

# 전류는 가장 바깥쪽(격자의 위쪽)에서 흘려준 전류가 안으로 침투될 수 있는지 확인

# M : 세로 크기 (2 ≤ M ≤ 1000)
# N : 가로 크기 (2 ≤ N ≤ 1000)
M, N = map(int, input().split())

board_list = []

for i in range(M):
    board = list(input().strip())
    board_list.append(board)

visited = [[0]*N for _ in range(M)]

def dfs(x, y):
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if board_list[nx][ny] == '0' and visited[nx][ny] == 0:
            dfs(nx, ny)

for i in range(N):
    if board_list[0][i] == '0' and visited[0][i] == 0:
        dfs(0, i)

if 1 in visited[M - 1]:
    print("YES")
else:
    print("NO")