import sys
import copy

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# N열 M행
N, M = map(int, input().split())
number_list = []

for i in range(N):
    number_list.append(list(map(int, input().split())))

# 이동은 오른쪽, 아래, 오른쪽 아래 대각선만 가능.
# 맨 마지막 점에서 현재 지점에서 큰 쪽으로 움직이는 건...?
# 아니면 이동하는 경로마다 누적합의 최대를 저장하자. <-이게 나을듯!

# 세 가지 이동이 불가능한 경우는
# 1. 오른쪽으로 이동이 불가한 경우(N행의 끝까지 왔을 때)
# 2. 아래로 이동이 불가한 경우(M열의 끝까지 왔을 때)
# 3. 오른쪽 아래 대각선으로 이동이 불가한 경우(N행의 끝까지 왔을 때. M열의 끝까지 왔을 때)
# 이 경우를 고려해서 코드를 짜보자.

number_add_list = copy.deepcopy(number_list)

for i in range(N):
    for j in range(M):
        # N행의 끝까지 왔을 때
        if j == M - 1:
            if i == N - 1:
                break
            # N행의 끝까지 왔을 때는 아래로만 이동 가능
            else:
                # 기존에 있는 값과, 현재 경로에서 더했을 때의 값중 더 큰 값을 해당 위치에 저장한다.
                number_add_list[i + 1][j] = max(number_add_list[i + 1][j], number_add_list[i][j] + number_list[i + 1][j])
        # M열의 끝까지 왔을 때
        elif i == N - 1:
            if j == M - 1:
                break
            else:
                # M열의 끝까지 왔을 때는 오른쪽으로만 이동 가능
                number_add_list[i][j + 1] = max(number_add_list[i][j + 1], number_add_list[i][j] + number_list[i][j + 1])
        else:
            # 아래 이동
            number_add_list[i + 1][j] = max(number_add_list[i + 1][j], number_add_list[i][j] + number_list[i + 1][j])
            # 오른쪽 이동
            number_add_list[i][j + 1] = max(number_add_list[i][j + 1], number_add_list[i][j] + number_list[i][j + 1])
            # 오른쪽 아래 대각선 이동
            number_add_list[i + 1][j + 1] = max(number_add_list[i + 1][j + 1], number_add_list[i][j] + number_list[i + 1][j + 1])
    
print(number_add_list[N - 1][M - 1])