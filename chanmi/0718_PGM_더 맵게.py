# 섞은 음식의 스코빌 지수 :
# 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수) * 2
# 최소 힙으로 0번째 인덱스를 찾으면 가장 맵지 않은 건 금방 찾을 수 있음.
# 그러면 두 번째로 맵지 않은 건 어떻게? -> 1번 인덱스

# 최소 힙은 2번 인덱스까지 사용해서 가장 작은 수, 두 번째로 작은 수, 세번째로 작은 수를 찾을 수 있음.
# 최소 힙은 부모 노드가 자식 노드보다 숫자가 작다는 특징이 있기 때문임.

import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    count = 0
    # scoville 안에 있는 값들이 전부 K 이상이게 만들고자 함.

    # 가장 작은 스코빌 지수 값들을 더해서 다시 최소 힙에 넣으면서
    # 최소 힙의 0번째 인덱스 값이 K 이상이 될 때까지 반복

    while scoville[0] < k:
        if len(scoville) == 1:
            return -1
        
        # 가장 맵지 않은 음식의 스코빌 지수
        first = heapq.heappop(scoville)
        # 두 번째로 맵지 않은 음식의 스코빌 지수
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first + second * 2)
        count += 1


    return count
