# 프로세스
from collections import deque
priorities = [2, 1, 3, 2]
queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])

print(queue)