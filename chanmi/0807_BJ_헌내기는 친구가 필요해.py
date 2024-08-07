import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 캠퍼스의 크기를 나타내는 두 정수 N, M (1 ≤ N, M ≤ 600)
# N : 세로 줄의 수
# M : 가로 줄의 수
N, M = map(int, input().split())

# O는 빈 공간, X는 벽, I는 도연이, P는 사람
# I의 위치에서 시작하면 됨

people_list = []
a, b = 0, 0

for i in range(N):
    people = list(input().strip())
    people_list.append(people)

    if 'I' in people:
        a, b = i, people.index('I')

visited = [[0] * M for _ in range(N)]
count = 0

def dfs(x, y):
    visited[x][y] = 1
    global count

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if people_list[nx][ny] == 'O' and visited[nx][ny] == 0:
            dfs(nx, ny)
        elif people_list[nx][ny] == 'P' and visited[nx][ny] == 0:
            count += 1
            dfs(nx, ny)
        elif people_list[nx][ny] == 'X':
            continue

dfs(a, b)

if count == 0:
    print("TT")
else:
    print(count)