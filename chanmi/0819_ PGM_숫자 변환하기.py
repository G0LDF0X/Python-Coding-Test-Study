from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    visited = set()

    while queue:
        current, count = queue.popleft()

        if current > y or current in visited:
            continue

        visited.add(current)
        if current == y:
            return count

        for i in (current * 2, current * 3, current + n):
            if i <= y and i not in visited:
                queue.append((i, count + 1))
    return -1