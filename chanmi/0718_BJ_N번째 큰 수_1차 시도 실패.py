import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

heap = []

# 연산의 수 N (1 <= N <= 1500)
n = int(input())

for i in range(n):
    number_list = input().split()
    for j in range(len(number_list)):
        heapq.heappush(heap, int(number_list[j]))

print(heap)
print(heap[-1 * n])