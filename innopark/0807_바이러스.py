# 첫째줄은 컴퓨터의 수
# 컴터 수는 100 이하인 양의 정수

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input().strip())            #컴터의 수
M = int(input().strip())            #연결 수 

graph = [[] for _ in range(N + 1)]      #input으로 주어지는 것이 1부터 주어져서 하나 더해줘야함.
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = 1
    for next in graph[node]:
        if visited[next] == 1:
            continue
        dfs(next)

dfs(1)
print(graph)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

print(visited)
# [0, 1, 1, 1, 0, 1, 1, 0]

print(sum(visited) - 1)
# 4
