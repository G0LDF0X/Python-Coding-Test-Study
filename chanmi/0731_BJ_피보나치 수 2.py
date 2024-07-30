import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1 <= N <= 90
N = int(input().strip())

dp = [0] * (N + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])