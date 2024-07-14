from collections import deque

def solution(priorities, location):
    answer = [] 
    queue = deque((i, j) for i, j in enumerate(priorities)) # 프로세스에 인덱스 부여
    
    while queue:
        process = queue.popleft()   
        if queue and any(process[1] < q[1] for q in queue): #우선 순위 높은게 있으면
            queue.append(process) # 큐에 다시 추가
        else: # 없으면
            answer.append(process) # 프로세스 실행
    
    # location 실행 순서 찾기
    for i in answer:
        if i[0] == location:
            return answer.index(i)+1