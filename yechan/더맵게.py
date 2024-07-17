def solution(scoville, K):
    answer = 0
    scoville.sort()
    if (scoville[1] != 0 ):
        while scoville[0]<K:
            scoville.insert(0,(scoville.pop(0)+scoville.pop(1)*2))
            scoville.sort()
            answer+=1
    else:
        answer-=1                        
    return answer
    

print(solution([1, 2, 3, 9, 10, 12], 7)) 