import sys
input = sys.stdin.read

# 각 케이스는 한 줄로 이루어져 있음
data = input().strip().split('\n')
case_number = 1

for line in data:
    L, P, V = map(int, line.split())
    if L == 0 and P == 0 and V == 0:
        break

    cycle = V // P
    remainder = V % P

    max_days = cycle*L + min(remainder, L)

    print(f"Case {case_number}: {max_days}")
    case_number += 1