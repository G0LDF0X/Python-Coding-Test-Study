from collections import deque

def can_reach_end(N, game_map):
    directions = [(1, 0), (0, 1)]
    que = deque([0, 0])
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True

    while que:
        x, y = que.popleft()
        if game_map[x][y] == -1:
            return "HaruHaru"
        jump_distance = game_map[x][y]
        for dx, dy in directions:
            nx, ny = x + dx * jump_distance, y + dy * jump_distance
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny))

    return "Hing"

N = int(input().strip())
game_map = [list(map(int, input().strip().split())) for _ in range(N)]



# 결과 출력
print(can_reach_end(N, game_map))






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