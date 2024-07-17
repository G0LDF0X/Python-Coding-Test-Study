from itertools import permutations

def solution(k, dungeons):
    answer = 0
    # 순열을 이용해 모든 가능한 경우의 수를 구함
    for i in permutations(dungeons, len(dungeons)):
        temp = k
        count = 0
        for essential, reduce in i:
            if temp >= essential:
                temp -= reduce
                count += 1    
        answer = max(count, answer)    
    return answer