#배추 흰지렁이를 구입한 한나.
# 가로길이 10
# 세로길이 8
# 배추 위치 개수 17
# (0,0) ~ (9,7)
# (0,0)(1,0)(1,1)(4,2)(4,3)(4,5)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input().split())

def dfs(x, y):
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if lettuce_list[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

for i in range(T):
    # M, N, K
    # M : 배추밭의 가로 길이 (1 ≤ M ≤ 50)
    # N : 배추밭의 세로 길이 (1 ≤ N ≤ 50)
    # K : 배추가 심어져 있는 위치의 개수 (1 ≤ K ≤ 2500)
    M, N, K = map(int, input().split())

    lettuce_list = [[0] * M for _ in range(N)]  #배추의 위치 표시를 위한 0
    visited = [[0] * M  for _ in range(N)]      #방문 여부를 담은 0

    for j in range(K):      #배추의 위치 표시 > 고로 개수만큼 반복
        X, Y = map (int, input().split())
        lettuce_list[X][Y] = 1
    
    result = 0
    for i in range(N):
        for j in range(M):
            if lettuce_list[i][j] == 1 and visited[i][j] == 0:      #배추가 있는데 방문하지 않았다면 result에서 하나를 더해준다.
                dfs(i, j)
                result += 1
    print(result)

