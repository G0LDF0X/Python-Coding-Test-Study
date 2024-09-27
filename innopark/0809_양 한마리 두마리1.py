import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input().strip())

location = []

def dfs(x, y):
    
    visited[x][y] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            continue

        if location[x][y] == '#' and location[nx][ny] == '#':
            dfs[nx][ny]
        elif location[x][y] == '#' and location[nx][ny] == '.':
            continue
        else:
            continue

            

for i in range(T):
    H, W = map(int, input().split())
    
    # visited = [[0]*W for _ in range(H)]
    for _ in range(H):
        location.append(list(input().strip()))

        visited = [[0]*W for _ in range(H)]

        dfs(0, 0)



