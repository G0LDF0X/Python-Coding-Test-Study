import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
#N이 세로 M이 가로
# print(f"N: {N}")
# print(f"M: {M}")


room_list = []

#-이게 가로로 인접해 있으면 1개
#|이게 세로로 인접해 있으면 1개
for i in range(N): #range안에는 세로
    room_list.append(list(input().strip()))



visited = [[0]*M for _ in range(N)]

def dfs(x, y, direction):
    visited[x][y] = 1

    if direction == '|':
        dx = [0, 0]
        dy = [-1, 1]
    elif direction == '-':
        dx = [-1, 1]
        dy = [0, 0]
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx > N or ny < 0 or ny >= M:
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
