import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
dot_list = []
distance_sum = 0

for i in range(N):
    x, y = map(int, input().split())
    dot_list.append((x, y))

# x축을 기준으로 정렬
dot_list.sort(key=lambda x: x[0])
x_middle_value = dot_list[N // 2][0]

# y축을 기준으로 정렬
dot_list.sort(key=lambda x: x[1])
y_middle_value = dot_list[N // 2][1]

for i in range(N):
    distance_sum += abs(x_middle_value - dot_list[i][0]) + abs(y_middle_value - dot_list[i][1])

print(distance_sum)
# 정렬해서 세우고 어떤 경계선을 그었을때 그 끝 사이의 거리

# 맨 처음에는 x, y 좌표의 평균으로 접근했는데 실제로 접근해보니 출력값과 다름.

