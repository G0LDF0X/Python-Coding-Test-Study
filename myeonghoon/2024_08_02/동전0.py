# 가지고 있는 동전의 갯수 : N개
# 지불해야 되는 금액 : K원
# 필요한 동전의 최소 갯수를 구하라.

# 4200원 -> 50000원을 4200원보다 큼, 10000원도 4200원보다 큼, 5000원도 4200원보다 큼, 1000원은 4200원보다 작음
# 4200원을 1000원으로 나눈 나머지는 잔돈 200원
# 1000원으로 나눈 나머지 값이 200원이기때문에 1000원보다 낮은 동전을 지불해야 한다. 1000원보다 낮은 동전은 500원이다.
# 500원은 200원보다 큼, 100원은 200보다 작음. 200 / 100하면 나머지가 0이고, 몫이 2가됨. 이건 동전의 갯수임
# 4200 / 1000 = 4
# 200 / 100 = 2
# 답은 6이다.


import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())


def solution(N, K):
    answer = 0
    coin_list = []

    for _ in range(N):
        coin_list.append(list(map(int, input().split()))) 

    coin_list = sorted(coin_list, reverse=True)

    for i in range(N):
        if coin_list[i][0] < K:
            answer += int(K / coin_list[i][0])
            K = K % coin_list[i][0]

            if K == 0:
                return answer     

print(solution(N, K))