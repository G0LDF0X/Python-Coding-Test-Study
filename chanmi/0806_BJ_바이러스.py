import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 컴퓨터의 수 N (1 ≤ N ≤ 100) (=노드의 개수)
N = int(input().strip())

# 네트워크 상에 연결되어있는 컴퓨터 수(=간선의 개수)
M = int(input().strip())

node_list = [[0] * N for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    node_list[x-1][y-1] = 1
    node_list[y-1][x-1] = 1

visited = [0] * N
count = -1

def dfs(x):
    global count
    visited[x] = 1
    count += 1

    for i in range(N):
        if node_list[x][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(0)

print(count)