import sys
import re

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

A, B = map(int, input().split())

# B를 2로 나누거나 뒤에서 1을 빼는 방식으로 진행.
# 짝수일 경우 2로 나누고, 짝수가 아닐 경우 뒤에 숫자 1이 있는지 확인해서
# 일의 자리가 1이라면 해당 숫자를 뺀다.

count = 0

while True:
    if A == B:
        count += 1
        break

    if A > B:
        count = -1
        break

    if B % 2 == 0:
        B //= 2
        count += 1
    else:
        if B % 10 == 1:
            B //= 10
            count += 1
        else:
            count = -1
            break

print(count)