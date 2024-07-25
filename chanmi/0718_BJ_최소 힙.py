import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

heap = []

# 연산의 수 N (1 <= N <= 100000)
n = int(input())

# 자연수가 들어오면 배열에 넣음
# 0이 들어오면 가장 작은값을 출력하고 해당 값을 제거

for i in range(n):
    command = int(input())

    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            min_num = heapq.heappop(heap)
            print(min_num)
    else:
        heapq.heappush(heap, command)