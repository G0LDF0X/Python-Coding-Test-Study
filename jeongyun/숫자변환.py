from collections import deque

def solution(x, y, n):
    answer = 0

    visited = set()  
    visited.add(x)
    
    q = deque([(x, 0)]) 

    while q:
        cur, cnt = q.popleft()

        if cur == y:
            answer = cnt
            return answer

        if cur * 3 <= y and cur * 3 not in visited:
            visited.add(cur * 3)
            q.append((cur * 3, cnt + 1))
        
        if cur * 2 <= y and cur * 2 not in visited:
            visited.add(cur * 2)
            q.append((cur * 2, cnt + 1))
        
        if cur + n <= y and cur + n not in visited:
            visited.add(cur + n)
            q.append((cur + n, cnt + 1))

    if answer == 0:
        answer = -1
    return answer