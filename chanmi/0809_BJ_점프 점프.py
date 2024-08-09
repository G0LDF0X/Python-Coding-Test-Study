import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 일렬로 놓인 돌의 개수 (1 ≤ N ≤ 100,000)
N = int(input().strip())

stone_list = list(map(int, input().split()))

# 출발점 s (1 ≤ s ≤ N)
s = int(input().strip())

# 한 번에 방문 가능한 돌만 세는 것이 아니라, 현재 지점에서 왼쪽으로 뛰었을 때, 그리고 오른쪽으로 뛰었을 때 모두를 세어야 함.

visited = [0] * N
count = 1

def dfs(x):
    global count
    visited[x] = 1

    dx = [stone_list[x], stone_list[x] * -1]

    for i in range(2):
        nx = x + dx[i]

        if 0 <= nx < N and visited[nx] == 0:
            count += 1
            dfs(nx)

dfs(s - 1)
print(count)