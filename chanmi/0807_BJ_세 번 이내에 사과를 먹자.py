import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 5*5 크기의 보드
# 1이면 사과, 0이면 빈 칸, -1이면 장애물
# r은 행 번호, c는 열 번호
# 학생은 (r, c)에서 출발
# 상하좌우중에 하나. 지나간 곳은 장애물 칸으로 변경됨.
# 세 번 이하의 이동으로 사과 두 개 이상 먹을 수 있으면 1, 그렇지 않으면 0

map_list = []
for i in range(5):
    apple = list(map(int, input().split()))
    map_list.append(apple)

r, c = map(int, input().split())
result = [0]

# 횟수 관리의 용이를 위해 count, apple_count는 패러미터로 넣어버림
def dfs(x, y, count, apple_count):
    if count > 3:
        return
    
    if apple_count >= 2:
        result[0] = 1
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue

        if map_list[nx][ny] == 0:
            map_list[nx][ny] = -1
            dfs(nx, ny, count + 1, apple_count)
            # dfs를 다 돌고 나면 다시 그 곳을 for문을 돌며 살펴볼 수 있으니 장애물 설정한 거 원상복귀하기
            map_list[nx][ny] = 0
        elif map_list[nx][ny] == 1:
            map_list[nx][ny] = -1
            dfs(nx, ny, count + 1, apple_count + 1)
            map_list[nx][ny] = 1
        elif map_list[nx][ny] == -1:
            continue
            
map_list[r][c] = -1
dfs(r, c, 0, 0)

print(result[0])