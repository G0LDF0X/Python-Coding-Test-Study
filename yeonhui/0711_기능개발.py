import math

def solution(progresses, speeds):
    worklist = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    answer = []
    front = 0

    for this in range(len(worklist)): # n번만 돌면 됨
        if worklist[this] > worklist[front]: # 지금일이 앞일보다 많이 걸림
            answer.append(this - front) # 지금일이 앞일에서 몇 순서 후인지 계산(그 사이 일만큼  결과에 저장)
            front = this # 지금 순서로 앞을 땡겨옴
    
    answer.append(len(worklist) - front) # 마지막 값은 루프에 안들어가니 따로 계산해서 추가

    return answer
