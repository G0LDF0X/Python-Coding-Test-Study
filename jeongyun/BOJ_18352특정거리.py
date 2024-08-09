import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1) 
visited[x] = 0

for i in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    
# print(graph)

q = deque([x])

while q:
    start = q.popleft()
    
    for dest in graph[start]:
        if visited[dest] == -1:
            visited[dest] = visited[start] + 1
            q.append(dest)
           
flag = False
 
for i in range(1, n+1):
    if visited[i] == k:
        print(i, end=' ')
        flag = True
if flag == False:
    print(-1)