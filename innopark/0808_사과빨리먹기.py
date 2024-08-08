import sys

input = sys.stdin.readline

location = []

for _ in range(5):
    location.append(list(input().split()))

x, y = map(int, input().split())

apple = 0

answer = []

# visited = [[0]*5 for _ in range(5)]


def dfs(x, y, count, apple, answer):
    if apple == 3:
        answer.append(count)
        return          #사과가 3개되면 count를 answer에 추가하고 함수 끝냄.
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx > 4 or ny < 0 or ny > 4:
            continue

        if location[nx][ny] == -1:
            continue
        
        if location[nx][ny] == 1:
            status = True
            apple += 1
        else:
            status = False

        cnt = location[x][y]
        location[x][y] = -1     #현재 위치를 장애물로 변경
        dfs(nx, ny, count + 1, apple, answer)
        location[x][y] = cnt    #재귀 호출이 끝나면 원래 상태로 복구. ?????

        if status:
            apple -= 1
        #현재 셀이 사과를 포함하고 있다면(location[nx][ny] == 1), 재귀 호출 전에 사과 개수를 증가시킵니다. 재귀 호출이 반환된 후, 백트래킹을 반영하기 위해 사과 개수를 감소시킵니다.

dfs(x, y, 0, apple, answer)

if len(answer) == 0:
    print(-1)
else:
    print(min(answer))