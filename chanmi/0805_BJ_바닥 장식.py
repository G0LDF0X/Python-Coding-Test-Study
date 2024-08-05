import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# N : 방 바닥의 세로 크기 (1 ≤ N ≤ 50)
# M : 방 바닥의 가로 크기 (1 ≤ M ≤ 50)
N, M = map(int, input().split())

room_list = []

# -가 인접해있고 같은 행에 있다면 같은 나무판자
# |가 인접해있고 같은 열에 있다면 같은 나무판자
for i in range(N):
    room_list.append(list(input().strip()))

visited = [[0] * M for _ in range(N)]

def dfs(x, y, direction):
    visited[x][y] = 1

    if direction == '-':
        dx = [0, 0]
        dy = [-1, 1]
    elif direction == '|':
        dx = [-1, 1]
        dy = [0, 0]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if room_list[nx][ny] == direction and visited[nx][ny] == 0:
            dfs(nx, ny, direction)

result = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i, j, room_list[i][j])
            result += 1

print(result)