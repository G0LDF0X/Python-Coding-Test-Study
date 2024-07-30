import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1 <= N <= 1000
N = int(input().strip())

# 상근 -> 찬영 순서로 진행.
# 1개 또는 3개를 가져갈 수 있음.

# 즉, 주어지는 숫자를 1과 3의 합으로 만들면 되는데,
# 먼저 3으로 최대한 가져간 다음에 1로 채우면 됨.

# 3으로 나눴을 때 나머지가 없고, 몫이 짝수라면 창영이의 승리, 홀수라면 상근이의 승리.
# 3으로 나눴을 때 나머지가 있고, 몫이 짝수라면 나머지가 홀수일 때 상근이의 승리, 짝수일 때 창영이의 승리.
# 3으로 나눴을 때 나머지가 있고, 몫이 홀수라면 나머지가 홀수일 때 창영이의 승리, 짝수일 때 상근이의 승리.

if N % 3 == 0:
    if N // 3 % 2 == 0:
        print("CY")
    else:
        print("SK")
else:
    if N // 3 % 2 == 0:
        if N % 3 % 2 == 1:
            print("SK")
        else:
            print("CY")
    else:
        if N % 3 % 2 == 1:
            print("CY")
        else:
            print("SK")