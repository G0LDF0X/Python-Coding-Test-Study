# N*N의 수, 각 수는 바로 위 수보다 큼 
# 이 때, N번째로 큰 수를 구해라 

# 최대힙 -> heapq 이용, push 할 때 부호를 바꿔서 넣어줌 . (-item, item)의 튜플의 형태 => 시간초과 

import sys
import heapq

n = int(sys.stdin.readline())
num = []

# 모두 입력받고 n번째 수 찾으려고 하면 메모리 초과 -> 최소힙의 크기를 n으로 유지 

for i in range(n):
    x = sys.stdin.readline().split()
    for j in x:
        y = int(j)
        if len(num) < n:
            heapq.heappush(num, y)
        else:
            if y> num[0]:
                heapq.heappop(num)
                heapq.heappush(num, y)
        
# n개의 가장 큰 수가 담긴 최소힙 -> 0번째 원소가 n번째로 큰 수 
print(num[0])