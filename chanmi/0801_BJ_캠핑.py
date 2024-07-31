import sys
import re

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# V를 P로 나눈 몫에 L을 곱하고,
# 해당 값에 나머지를 더해주면 된다.

count = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    else:
        print("Case", str(count) + ":", (V // P) * L + min(V % P, L))
        count += 1