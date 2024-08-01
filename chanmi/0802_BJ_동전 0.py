import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 동전은 총 N 종류고, 이 동전으로 가치 K를 만들 때
# 필요한 동전 개수의 최소값을 구하는 프로그램.

# 1 ≤ N ≤ 10
# 1 ≤ K ≤ 100,000,000
N, K = map(int, input().split())
money_list = []

for i in range(N):
    money_list.append(int(input().strip()))

# 내림차순으로 정렬(큰 돈부터 안 맞으면 빨리빨리 넘기기 위해서)
money_list.sort(reverse=True)

money_count = 0

for money in money_list:
    # 화폐가 K보다 큰 경우 그 화폐는 쓰지 않음
    if money > K:
        continue
    else:
        # 해당 화폐로 만들 수 있는 최대 개수를 더해줌
        money_count += K // money
        K %= money

print(money_count)