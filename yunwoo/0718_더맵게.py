import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 주어진 리스트를 힙으로 변환
    mix_count = 0

    #특정 조건 달성 할 때 까지 반복때문에  while문 사용
    while len(scoville) > 1 and scoville[0] < K:
        # 스코빌 지수 제일 낮은 음식 두개를 꺼내서 섞음(섞음으로 인해 개체가 하나 줄어듦)
        # 힙큐 자료구조 특성으로인해 낮은것 부터 자동 카운팅
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_food = first + (second * 2)
        heapq.heappush(scoville, new_food)
        mix_count += 1

    # 모든 음식의 스코빌 지수가 K 이상인지 확인
    if scoville[0] < K:
        return -1
    return mix_count