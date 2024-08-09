import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(start_x, start_y):
    global min_move
    q = deque()
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, move_count = q.popleft()

        if maze_list[x][y] == "G":
            min_move = min(min_move, move_count)
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and maze_list[nx][ny] != "X" and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, move_count + 1))

T = int(input().strip())

for _ in range(T):
    # R : 세로의 크기 (1 ≤ R ≤ 15)
    # C : 가로의 크기 (1 ≤ C ≤ 15)
    R, C = map(int, input().split())

    maze_list = []
    start_index = [0, 0]
    for i in range(R):
        maze = list(input().strip())
        if "S" in maze:
            start_index[0] = i
            start_index[1] = maze.index("S")
        maze_list.append(maze)

    visited = [[0]*C for _ in range(R)]
    min_move = float("inf")

    bfs(start_index[0], start_index[1])
    if min_move == float("inf"):
        print("No Exit")
    else:
        print("Shortest Path:", min_move)