from math import comb 

def solution(clothes):
    answer = 1
    cloth = {}
    
    for item, type in clothes:
        if type in cloth.keys():
            cloth[type]+= [item]
        else:
            cloth[type] = [item]
    # print(cloth.items())
    
    for _, item in cloth.items():
        answer *= (len(item) + 1)
        
    return answer-1