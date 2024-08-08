import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 보드의 크기는 5*5
# r은 행 번호, c는 열 번호
# 상하좌우로 이동
# 이동한 칸은 장애물 있는 칸으로 변경
# 사과 3개를 먹기 위한 최소 이동 횟수
# 못 먹으면 -1 출력

board_list = []
for i in range(5):
    board = list(map(int, input().split()))
    board_list.append(board)

# 학생의 현재 위치
r, c = map(int, input().split())
min_move = float('inf')

def dfs(x, y, apple_count, move):
    board_list[x][y] = -1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if board_list[nx][ny] == 1:
            if apple_count + 1 == 3:
                global min_move
                min_move = min(min_move, move + 1)
                return
            else:
                dfs(nx, ny, apple_count + 1, move + 1)
                board_list[nx][ny] = 1
        elif board_list[nx][ny] == 0:
            dfs(nx, ny, apple_count, move + 1)
            board_list[nx][ny] = 0

dfs(r, c, board_list[r][c], 0)

if min_move == float('inf'):
    print(-1)
else:
    print(min_move)