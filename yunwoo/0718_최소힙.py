import heapq
import sys

input = sys.stdin.read
heap = []

# 입력을 한 번에 받아서 처리
data = input().strip().split()

for value in data:
    num = int(value)
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
