import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 농장 크기 : 10 * 10
# B : 불이 난 헛간
# L : 호수
# R : 바위 위치

farm_list = []
fire_index = [0, 0]

for i in range(10):
    farm = list(input().strip())
    if "B" in farm:
        fire_index[0] = i
        fire_index[1] = farm.index("B")
    farm_list.append(farm)

visited = [[0]*10 for _ in range(10)]
min_move = float("inf")

def bfs(start_x, start_y):
    global min_move
    q = deque()
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, move_count = q.popleft()

        if farm_list[x][y] == "L":
            min_move = move_count
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 10 and 0 <= ny < 10 and farm_list[nx][ny] != "R" and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, move_count + 1))

bfs(fire_index[0], fire_index[1])
print(min_move - 1)