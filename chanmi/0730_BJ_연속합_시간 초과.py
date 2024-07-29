import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1 ≤ N ≤ 100000
N = int(input().strip())

number_list = list(map(int, input().split()))

# 현재 리스트에서 연속합을 구해야 하기 때문에 정렬은 사용 불가

# 가장 큰 수를 찾은 뒤,
# 큰 수를 기준으로 좌, 우를 하나씩 더했을 때의 최댓값을 찾아서 더하는 건?

max_number = max(number_list)
max_index = 0

for i, v in enumerate(number_list):
    if v == max_number:
        max_index = i
        break

max_left_sum = -1001
max_right_sum = -1001

for i in range(max_index, -1, -1):
    max_left_sum = max(max_left_sum, sum(number_list[i:max_index+1]))

for i in range(max_index, N):
    max_right_sum = max(max_right_sum, sum(number_list[max_index:i+1]))

print(max_left_sum + max_right_sum - max_number)