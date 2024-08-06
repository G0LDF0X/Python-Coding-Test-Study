# from collections import deque

# def can_reach_end(N, game_map):
#     directions = [(1, 0), (0, 1)]
#     que = deque([0, 0])
#     visited = [[False] * N for _ in range(N)]
#     visited[0][0] = True

#     while que:
#         x, y = que.popleft()
#         if game_map[x][y] == -1:
#             return "HaruHaru"
#         jump_distance = game_map[x][y]
#         for dx, dy in directions:
#             nx, ny = x + dx * jump_distance, y + dy * jump_distance
#             if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 que.append((nx, ny))

#     return "Hing"

# N = int(input().strip())
# game_map = [list(map(int, input().strip().split())) for _ in range(N)]



# # 결과 출력
# print(can_reach_end(N, game_map))



# 1단계 N 받고, graph 받아오기
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#게임 구역의 크기는 N이다. (2 또는 3)
N = int(input().strip())
graph = []

print(f"N : {N}")

for i in range(N):
    graph.append(list(map(int, input().split())))

# print(f"GRAPH : {graph}")
# GRAPH : 
# [[1, 1, 10], 
# [1, 5, 1], 
# [2, 2, -1]]

visited = [[0]*N for _ in range(N)]
print(visited)

# visited = 
# [[0, 0, 0], 
# [0, 0, 0], 
# [0, 0, 0]]

def dfs(x, y):
    visited[x][y] = 1

    dx = [graph[x][y], 0]
    dy = [0, graph[x][y]]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        if visited[nx][ny] == 0:
            dfs(nx, ny)

dfs(0, 0)            

if visited[N-1][N-1] == 1:
    print("HaruHaru")
else:
    print("Hing")









# def count_wood_planks(N, M, floor):
#     visited = [[False] * M for _ in range(N)]
#     plank_count = 0

#     def dfs(x, y, char):
#         stack = [(x, y)]
#         while stack:
#             cx, cy = stack.pop()
#             if visited[cx][cy]:
#                 continue
#             visited[cx][cy] = True
#             if char == '-':
#                 if cy + 1 < M and floor[cx][cy + 1] == '-' and not visited[cx][cy + 1]:
#                     stack.append((cx, cy + 1))
#             elif char == '|':
#                 if cx + 1 < N and floor[cx + 1][cy] == '|' and not visited[cx + 1][cy]:
#                     stack.append((cx + 1, cy))

#     for i in range(N):
#         for j in range(M):
#             if not visited[i][j]:
#                 plank_count += 1
#                 dfs(i, j, floor[i][j])

#     return plank_count

# # 입력 받기
# N, M = map(int, input().split())
# floor = [input().strip() for _ in range(N)]

# # 결과 출력
# print(count_wood_planks(N, M, floor))