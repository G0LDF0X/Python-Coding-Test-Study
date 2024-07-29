import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())

# 설탕 3kg, 5kg가 있음
# 최대한 적은 봉지 사용
# 정확히 배달 못하면 -1 반환

# 설탕의 종류
# 1. 5로 나누어 떨어지는 경우
# 2. 5와 3의 조합으로 나누어 떨어지는 경우
# 3. 3으로 나누어 떨어지는 경우
# 4. 5와 3으로 나눌 수 없는 경우(-1 반환)

# 따라서 먼저 5로 나누어 떨어지는 경우를 구하고,
# 이후 3으로 나눌 수 있는지 확인하면 된다.

vynil_count = 0

while N > 0:
    if N % 5 == 0:
        vynil_count += N // 5
        N = 0
    else:
        N -= 3
        vynil_count += 1
        if N < 0:
            vynil_count = -1
            break

print(vynil_count)