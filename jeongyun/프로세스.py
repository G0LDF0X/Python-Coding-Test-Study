def solution(priorities, location):
    answer = 1
    waiting = []
    n = len(priorities)
    
    # 우선순위값과 인덱스를 함께 저장하는 process 리스트
    for i in range(n):
        waiting.append((priorities[i], i))
        
    # print(waiting)
    
    # 모든 프로세스를 다 실행할 때까지 process = waiting의 첫번째 프로세스
    while len(waiting) >0:
        
        run = True  # 현재 프로세스가 실행할 수 있는 지 여부 확인 위한 변수 
        process = waiting[0]
        waiting = waiting[1:]
        # print(process)
        # 남은 waiting의 프로세스 중 process 보다 우선순위 높은 게 있는지 확인 -> 있으면 waiting에 process 다시 추가
        for w in waiting:
            # print(process[0], w[0])
            if process[0] <w[0]:
                waiting.append(process)
                run = False     # 현재 프로세스 실행 불가 
                break
        # 현재 프로세스 실행 가능
        if run == True: 
            # print(answer, process)
            # 현재 프로세스의 인덱스가 location과 같으면 return 
            if process[1] == location:
                return answer
            answer +=1
        
    return answer