import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# N : 소의 마리수 (1 ≤ N ≤ 250)
# M : 소끼리 연결된 밧줄의 쌍 (1 ≤ M ≤ N*(N-1)/2)

N, M = map(int, input().split())

rope_list = [[] for _ in range(N + 1)]

for i in range(M):
    c1, c2 = map(int, input().split())
    rope_list[c1].append(c2)
    rope_list[c2].append(c1)

# 소1과 로프로 연결되지 않은 소의 수를 오름차순으로 출력
visited = [0] * (N + 1)

def bfs(start_x):
    q = deque()
    q.append(start_x)
    visited[start_x] = 1

    while q:
        x = q.popleft()

        for i in rope_list[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    
bfs(1)

if 0 in visited[1:]:
    for i in range(1, N + 1):
        if visited[i] == 0:
            print(i)
else:
    print(0)