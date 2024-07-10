from math import ceil

def solution(progresses, speeds):
    answer = [1]
    success = []
    num = len(progresses)
    
    
    for i in range(num):
        work = 100 - progresses[i]
        success.append(ceil(work/speeds[i]))
        
    prev = success[0]
    idx = 0
    
    for i in range(1, num):
 
        if success[i] <=prev :
            answer[idx] +=1
        else:
            idx +=1
            prev = success[i]
            answer.append(1)
            
    return answer