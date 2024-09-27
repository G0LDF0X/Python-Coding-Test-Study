from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)]) #현재 값, 연산 횟수
    visited = set()
    visited.add(x)
    
    while queue:
        current, steps = queue.popleft()
        
        if current == y:
            return steps
        
        #가능한 연산
        #case1
        next_add = current + n
        if next_add <= y and next_add not in visited:
            visited.add(next_add)
            queue.append((next_add, steps + 1))
            
        #case2
        next_mul2 = current * 2
        if next_mul2 <= y and next_mul2 not in visited:
            visited.add(next_mul2)
            queue.append((next_mul2, steps + 1))
            
        #case3
        next_mul3 = current * 3
        if next_mul3 <= y and next_mul3 not in visited:
            visited.add(next_mul3)
            queue.append((next_mul3, steps + 1))
    return -1
        