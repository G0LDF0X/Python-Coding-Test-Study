import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 테스트 케이스의 개수 T
T = int(input().strip())

def dfs(x, y):
    visited[x][y] = 1

    # x가 감소하는 경우, 증가하는 경우, 그 외(y가 증감하는 경우들)
    dx = [-1, 1, 0, 0]

    # y가 감소하는 경우, 증가하는 경우, 그 외(x가 증감하는 경우들)
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 만약 위아래좌우로 이동했는데 바깥으로 나가는 경우는 무시
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 만약 1이 연결되어 있는데 방문 안 한 노드라면 바로 이동
        if lettuce_list[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

for i in range(T):
    # M, N, K
    # M : 배추밭의 가로 길이 (1 ≤ M ≤ 50)
    # N : 배추밭의 세로 길이 (1 ≤ N ≤ 50)
    # K : 배추가 심어져 있는 위치의 개수 (1 ≤ K ≤ 2500)
    M, N, K = map(int, input().split())

    lettuce_list = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for j in range(K):
        # X, Y
        # X : 배추의 가로 위치 (0 ≤ X ≤ M-1)
        # Y : 배추의 세로 위치 (0 ≤ Y ≤ N-1)
        X, Y = map(int, input().split())
        lettuce_list[Y][X] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            # 1이 있고 한 번도 방문 안 한 곳들에 대해 dfs 실행
            if lettuce_list[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                result += 1
    
    print(result)

    # 각 테스트 케이스에서는 1로 표기된 구간이 몇 개인지 출력 (이어져 있는 곳은 한 구간으로 간주)