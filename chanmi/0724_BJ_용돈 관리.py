import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# N일 동안 사용한 금액 계산
# M번만 통장에서 돈을 빼서 쓰기로

# K원을 인출하여 모자라면 
# 남은 금액이 그날 사용할 금액보다 많아도 통장에 넣고 M번을 맞추기 위해 K원 인출 가능.


# 7 5
# 100
# 400
# 300
# 100
# 500
# 101
# 400

# 출력 : 500

# M = 5이므로 총 5회 인출
# 돈이 부족하면, 수중에 있는 돈을 다 쓴 뒤 인출하는 것이 아니라 현재 돈을 통장에 넣고 다시 K원을 인출함.
# 또한 남은 용돈이 다음 날로 넘어가, 그 다음 날에 사용되는 경우까지 함께 계산해야 함.

# 즉, K원은 모든 소비를 합한 값보다는 작거나 같아야하고, 일일 사용량의 최댓값보다는 크거나 같아야 함.
# 하루에 모든 날짜를 다 소비할 수 있는 만큼의 돈을 뽑으면 남은 날짜는 원하는 만큼 M번에 맞출 수 있기 때문.

N, M = map(int, input().split())
money_list = []

for i in range(N):
    money = int(input())
    money_list.append(money)

min_money = max(money_list)
max_money = sum(money_list)

answer = 0

while min_money <= max_money:
    mid_value = (min_money + max_money) // 2

    # 맨 처음 1일차에 빌리는 돈
    count = 1

    # 현재 가진 돈
    charge = mid_value
    
    for i in range(N):
        if charge < money_list[i]:
            count += 1
            charge = mid_value
        charge -= money_list[i]

    # M번 초과로 인출하는 경우 : 돈을 좀 더 많이 빌려보기(start값 늘리기)
    if count > M:
        min_money= mid_value + 1
    # M번 이하로 인출 가능한 경우 : 돈을 좀 더 적게 빌려보기(end값 줄이기)
    else:
        max_money = mid_value - 1
        answer = mid_value

print(answer)