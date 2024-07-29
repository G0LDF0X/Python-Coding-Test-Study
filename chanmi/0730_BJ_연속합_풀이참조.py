import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1 ≤ N ≤ 100000
N = int(input().strip())

number_list = list(map(int, input().split()))

# 시간 초과가 뜨는 이유 : N의 길이가 10만이나 되기 때문에, 모든 리스트를 돌며 더하다보면 오래 걸리는듯...
# https://hongjw1938.tistory.com/61 (풀이 참조)

max_current = number_list[0]
max_global = number_list[0]

for i in range(1, N):
    max_current = max(number_list[i], max_current + number_list[i])
    if max_current > max_global:
        max_global = max_current

print(max_global)