import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# N : 정점의 개수 (1 ≤ N ≤ 1000)
# M : 간선의 개수 (1 ≤ M ≤ N * (N - 1) / 2)
N, M = map(int, input().split())
node_list = [[0] * N for _ in range(N)]
visited = [0] * N

for i in range(M):
    # 간선의 양 끝점 u, v (1 ≤ u, v ≤ N, u ≠ v)
    u, v = map(int, input().split())
    node_list[u - 1][v - 1] = 1
    node_list[v - 1][u - 1] = 1

def dfs(x):
    visited[x] = 1

    for i in range(N):
        if node_list[x][i] == 1 and visited[i] == 0:
            dfs(i)

result = 0
for i in range(N):
    if visited[i] == 0:
        dfs(i)
        result += 1

print(result)