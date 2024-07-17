from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    # 던전의 모든 순열을 생성한다.
    for perm in permutations(dungeons):
        current_fatigue = k
        count = 0
        # 순열에 따라 던전을 탐험한다.
        for minimum, consumption in perm:
            if current_fatigue >= minimum:
                current_fatigue -= consumption
                count += 1
            else:
                break
        max_dungeons = max(max_dungeons, count)
    
    return max_dungeons

# 테스트 케이스
k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

print(solution(k, dungeons))
