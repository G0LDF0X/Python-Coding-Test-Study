from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = deque([0] * bridge_length)  
    weights = deque(truck_weights) 
    
    cur = 0
    while weights:
        answer = answer + 1

        cur -= bridge.popleft()

        if cur + weights[0] <= weight:
            cur += weights[0]
            bridge.append(weights.popleft())
        else: 
            bridge.append(0)
            
    answer += bridge_length
    
    return answer