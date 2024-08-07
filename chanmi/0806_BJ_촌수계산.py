import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 전체 사람 N (1 ≤ N ≤ 100)
N = int(input().strip())

# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
first, second = map(int, input().split())

# 부모 자식들 간의 관계 개수 M
M = int(input().strip())

# 부모 자식들 간의 관계를 나타내는 두 정수 x, y
# 이때 x는 y의 부모
people_list = [[0] * N for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    people_list[x-1][y-1] = 1
    people_list[y-1][x-1] = 1

# first와 second 사이의 줄 개수?를 count 하면 됨.

visited = [0] * N
count = -1
is_found = False

def dfs(x, y, count):
    global is_found
    visited[x] = 1
    count += 1

    if x == y:
        is_found = True
        print(count)
        return

    for i in range(N):
        if people_list[x][i] == 1 and visited[i] == 0:
            dfs(i, y, count)
        if visited[y] == 1:
            return
        
dfs(first-1, second-1, count)

if not is_found:
    print(-1)