def solution(clothes):
    answer = 1
    closet = {}
    for _,k in clothes:
        if k in closet:
            closet[k] +=1
        else:
            closet[k] = 1
        print(closet[k])
    for k in closet :
        answer *= closet[k]+1
        
    return answer-1