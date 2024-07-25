import heapq
import sys

input = sys.stdin.readline


def solution(n):
    heap = []

    for _ in range(n):

        x = int(input())        
            
        if x == 0:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)
        else:
            heapq.heappush(heap, x)



solution(int(input()))



# 배열에 자연수 x를 넣는다. 0이 아닌 type int라면
# x가 0이라면 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32