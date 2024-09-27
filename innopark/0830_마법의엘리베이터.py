from collections import deque

def solution(storey):
    queue = deque([(storey, 0)])  # (현재 층, 버튼 누른 횟수)
    visited = set()  # 방문한 층을 기록하기 위한 집합

    while queue:
        current, steps = queue.popleft()

        if current == 0:
            return steps

        if current in visited:  #이미 방문한 층은 넘기기 위함. 왜 넘겨야 하는가 ??
            continue

        visited.add(current)

        for move in [1, -1, 10, -10, 100, -100, 1000, -1000, 10000, -10000, 100000, -100000, 1000000, -1000000, 10000000, -10000000]:
            next_floor = current + move
            if next_floor >= 0 and next_floor not in visited:
                queue.append((next_floor, steps + 1))

    return -1  # 이론적으로 이 부분은 실행되지 않음

# 테스트 케이스
print(solution(16))  # 6
# print(solution(2554))  # 16

# 어떻게 최소 횟수가 바로 반환이 되는가 ?
# 그 이유는 먼저 현재 층이 0층이 되는 경우가 나올 때, steps가 반환되니까.
