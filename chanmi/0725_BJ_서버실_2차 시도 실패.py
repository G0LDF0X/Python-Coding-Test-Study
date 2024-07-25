import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())

computer_list = []

# append : 리스트 끝에 단일 요소를 추가. list를 append하면 다차원 배열이 됨.
# extend : 리스트 끝에 다른 리스트의 모든 요소를 추가. 즉, 리스트를 병합하는데 사용됨.
for i in range(N):
    computer_list.extend(list(map(int, input().split())))

computer_list.sort()

# 정렬을 하면 이렇게 됨
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9]

# 0을 제외하고 컴퓨터가 있는 것만 살피면
# [1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9]
# 해당 리스트의 값을 모두 더한 게 컴퓨터의 총 대수가 됨.
# 이 총 컴퓨터의 대수의 절반 이상이 켜지는 시간을 출력하면 됨.

# 1분 경과 : 전체 컴퓨터 중 20대가 켜짐
# 2분 경과 : 36대가 켜짐 (+16대)
# 3분 경과 : 50대가 켜짐 (+14대)
# 4분 경과 : 62대가 켜짐 (+12대)
# 5분 경과 : 71대가 켜짐 (+9대)
# 6분 경과 : 77대가 켜짐 (+6대)
# 7분 경과 : 82대가 켜짐 (+5대)
# 8분 경과 : 84대가 켜짐 (+2대)
# 9분 경과 : 85대가 켜짐 (+1대)

# 최소값 : 1분이 지나면 모든 컴퓨터가 켜지는 경우이므로, 1
# 최댓값 : 컴퓨터가 한 칸에 모두 쌓여있는 경우이므로 리스트에 있는 모든 원소의 합

start = 1
end = sum(computer_list)

if sum(computer_list) % 2 == 0:
    mid_value = sum(computer_list) // 2
else:
    mid_value = sum(computer_list) // 2 + 1

answer = 0

while start <= end:
    # on_time : 냉각기를 켠 시간
    on_time = (start + end) // 2

    computer_sum = 0

    # 냉각기를 켰을 때 꺼지는 컴퓨터의 수를 더하기
    for computer in computer_list:
        if computer > on_time:
            computer_sum += on_time
        else:
            computer_sum += computer

    # 컴퓨터를 충분히 켠 경우에는, 냉각기 켜는 시간 줄이기.
    # 즉, end를 감소시키면 됨.
    if computer_sum >= mid_value:
        end = on_time - 1
        answer = on_time

    # 컴퓨터가 모자란 경우에는, 냉각기를 더 많이 켜야함.
    # 즉, start를 증가시키면 됨.
    else:
        start = on_time + 1

print(answer)