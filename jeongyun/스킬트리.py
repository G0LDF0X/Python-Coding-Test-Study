def solution(skill, skill_trees):
    answer = 0
    skill_seq = []
    
    for s in skill:
        skill_seq.append(s)
        
    for skill_tree in skill_trees:
        prev = -1
        flag = True
        
        for t in skill_tree:
            
            # 각 스킬이 seq 에 있으면 그 인덱스 비교 
            if t in skill_seq:
                cur = skill_seq.index(t)
                # 1차이가 나면 가능 아니면 불가능 
                if cur == prev+1:
                    prev = cur
                else:
                    flag = False
                    break
                flag = True
            
        if flag:
            # print(skill_tree)
            answer +=1
            
    return answer