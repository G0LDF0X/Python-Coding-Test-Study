grid = [input().strip() for _ in range(10)] 

# 위치 찾기    B / R / L
for i in range(10):
    for j in range(10):
        if grid[i][j] == "B":
            barn = (i, j)
        elif grid[i][j] == "L":
            lake = (i, j)
        elif grid[i][j] == "R":
            rock = (i, j)

# BFS 탐색
def bfs(start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(start[0], start[1], 0)]  # (x, y, distance)
    visited = [[False] * 10 for _ in range(10)]
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.pop(0)

        if (x, y) == end:
            return dist -1  #시작점과 끝점을 제외한 '.'의 개수

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny] and grid[nx][ny] != 'R':
                visited[nx][ny] = True      #위치가 바위가 아니고 grid 내에 있으면 그 위치를 queue에 추가한다.
                queue.append((nx, ny, dist + 1))
                print(queue)
    return -1

print(bfs(lake, barn))
