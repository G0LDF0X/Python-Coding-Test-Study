import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

heap = []

# 연산의 수 N (1 <= N <= 1500)
n = int(input())

for i in range(n):
    number_list = input().split()

    # heap에 아무것도 없을 경우
    if len(heap) == 0:
        for j in range(len(number_list)):
            heapq.heappush(heap, int(number_list[j]))

    # heap에 원소가 있고, 길이를 N 이하로 유지하기
    else:
        # 최소 힙의 가장 앞, 0번째 인덱스에는 그 heap에서 가장 작은 원소가 위치한다.
        # 해당 원소보다 큰 값만 push하고, 작은 값은 pop 하다보면
        # heap의 길이를 N으로 잘랐을 때,
        # 결국 heap[0]에 N번째로 큰 수가 위치하게 된다.
        for num in number_list:
            if heap[0] < int(num):
                heapq.heappush(heap, int(num))
                heapq.heappop(heap)
print(heap[0])