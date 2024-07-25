import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
number_list = list(map(int, input().split()))
K = int(input().strip())

# 시간 초과가 나온 이유는 

start = 0
list_count = 0
current_sum = 0

for end in range(N):
    # 현재 [start, end] 사이의 합을 current_sum에 저장한다.
    current_sum += number_list[end]

    # 만약 [start, end] 사이의 합이 K보다 크다면
    # end보다 뒤에 있는 원소들 역시 더해도 K보다 크므로 list_count에 N - end를 더하고
    # [start, end]가 K보다 작아지거나 start > end가 될 때까지 start를 증가시킨다.
    # 이때, start를 옮기면서 current_sum에서 number_list[start]를 빼준다.
    while current_sum > K and start <= end:
        list_count += N - end
        current_sum -= number_list[start]
        start += 1

print(list_count)