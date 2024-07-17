import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # print(scoville)

    # 음식이 2개 이상이고 값이 K 이하일 때 계속 섞기
    while len(scoville) >=2 and scoville[0] < K:
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        
        # 음식 섞기 
        new_scoville = x + 2*y
        heapq.heappush(scoville, new_scoville)
        
        answer +=1
        
    # 음식이 1개 남았을 때 값 비교 
    if scoville[0] <K:
        answer = -1
        
    return answer