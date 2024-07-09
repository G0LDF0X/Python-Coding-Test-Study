def solution(clothes):
    answer = 1
    clothes_dict = dict()
    for c in clothes:
        if c[1] in clothes_dict:
            clothes_dict[c[1]] += 1
        else:
            clothes_dict[c[1]] = 1
    for key in clothes_dict.keys():
        answer *= (clothes_dict[key]+1)
    answer -= 1
    return answer
