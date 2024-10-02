from collections import defaultdict

def solution(weights):
    answer = 0
    
    # weight 를 키로 하는 딕셔너리 , value는 갯수 
    d_weight = defaultdict(int)
    
    for weight in weights :
        d_weight[weight] += 1
    
    for key, val in d_weight.items() :
        # 2개 이상이면 조합의 갯수 구하기
        if val > 1 :
            answer += val * ( val - 1) // 2
        # 무게 * 2, 3, 4 해보면서 조합 구하기 
        if key*2 in d_weight :
            answer += val * d_weight[key*2]
        if key*3 % 2 == 0 and key*3 // 2 in d_weight :
            answer += val * d_weight[key*3 // 2]
        if key*4 % 3 == 0 and key*4 // 3 in d_weight :
            answer += val * d_weight[key*4 // 3]

    return answer

