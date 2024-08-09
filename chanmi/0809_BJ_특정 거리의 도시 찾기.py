import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 도시의 개수 N (2 ≤ N ≤ 300,000)
# 도로의 개수 M (1 ≤ M ≤ 1,000,000)
# 거리 정보 K (1 ≤ K ≤ 300,000)
# 출발 도시 X (1 ≤ X ≤ N)

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(M):
    start, end = map(int, input().split())
    graph[start - 1].append(end - 1)

visited = [0] * N

def bfs(start_x):
    q = deque()
    q.append((start_x, 0))
    visited[start_x] = 1
    result = []

    while q:
        x, move_count = q.popleft()

        if move_count == K:
            result.append(x + 1)
        
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append((i, move_count + 1))
    
    if result:
        result.sort()
        for data in result:
            print(data)
    else:
        print(-1)
        
bfs(X - 1)