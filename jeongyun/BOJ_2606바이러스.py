from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

visited[1] = 1

q = deque([1])

while q:
    v = q.popleft()
    for i in graph[v]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
            
print(visited.count(1)-1)            