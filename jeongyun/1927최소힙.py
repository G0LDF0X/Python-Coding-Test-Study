# 최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
# 파이썬의 heapq : 최소힙 

import sys
import heapq

heap = []

n = int(sys.stdin.readline())

for i in range(n):
    x = int(sys.stdin.readline())
    
    # 자연수
    if x >0:
        heapq.heappush(heap, x)
    elif x == 0:
        print(0) if len(heap)<=0 else print(heapq.heappop(heap))
    