import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 숫자 판의 크기는 5*5로 고정
# 안에 0~9까지의 숫자가 적혀 있음
# 임의의 위치에서 시작해, 상하좌우로 5칸 이동.
# 이동하면서 각 칸에 있는 숫자를 차례로 붙이면 6자리 숫자가 됨.
# 이동했던 칸 다시 이동하기 가능
# 0으로 시작하는 000123 만들기 가능

number_list = []
tmp_number_list = []
unique_number_list = []
count = 0

for i in range(5):
    number = list(map(int, input().split()))
    number_list.append(number)

def dfs(x, y):
    global count
    tmp_number_list.append(number_list[x][y])
    count += 1

    if count == 6:
        final_number = int(''.join(map(str, tmp_number_list)))
        if final_number not in unique_number_list:
            unique_number_list.append(final_number)
        return
    else:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue

            dfs(nx, ny)
            # for i in range(4)를 돌면서 다른 숫자도 돌아야 하니까 방금 갔던 숫자 제외해줘야함
            count -= 1
            tmp_number_list.pop()

for i in range(5):
    for j in range(5):
        dfs(i, j)
        count = 0
        tmp_number_list = []

print(len(unique_number_list))