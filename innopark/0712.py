from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    answer = 0
    
    while queue:
        idx, priority = queue.popleft()
        if queue and max(queue, key=lambda x: x[1])[1] > priority:
            queue.append((idx, priority))
        else:
            answer += 1
            if idx == location:
                break
    
    return answer