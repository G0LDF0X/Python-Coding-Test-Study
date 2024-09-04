from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # 각 코스 값에 따른 조합의 빈도 수를 저장할 딕셔너리 -> 카운터 사용
    candi_cnt = {c: Counter() for c in course}

    # orders에서 c개로 만들 수 있는 조합 만들기
    for order in orders:
        for c in course:
            for comb in combinations(sorted(order), c):
                candi_cnt[c][comb] += 1

    # 각 코스 길이에 대해 가장 많이 주문된 조합 찾기
    for c in course:
        if candi_cnt[c]:  
            max_count = max(candi_cnt[c].values())
            # 주문 2번 이상일때만 answer 에 저장
            if max_count > 1: 
                for comb, count in candi_cnt[c].items():
                    if count == max_count:
                        answer.append(''.join(comb))

    # answer 사전순 정렬
    answer.sort()
    return answer

## 시간초과 풀이 
# from itertools import combinations, permutations

# def solution(orders, course):
#     answer = []
#     answers = []
#     candidates = []
#     candi_cnt = dict()
#     sorted_candi_cnt = dict()

#     # orders에서 조합 만들기 -> permutations 사용. 각order에서 가능한 모든 c개의 조합 생성 -> candidates 에 저장 
#     for c in course:
#         for order in orders:
#             perms = permutations(order, c)
#             for perm in perms:
#                 candidates.append(perm)
#     candidates.sort(key = lambda x: (len(x), x))
    
#     # candidates 에서 각 조합의 주문 수 체크. -> 주문수가 가장 많은 조합만 answer에 저장 -> 주문수를 candi_cnt  딕셔너리에 저장 
    
#     for can in candidates:
#         if can in candi_cnt.keys():
#             candi_cnt[can] +=1
#         else:
#             candi_cnt[can] = 0

#     # 주문 수 기준으로 내림차순 정렬
#     sorted_candi_cnt = sorted(candi_cnt.items(), key = lambda item : (len(item[0]), item[1]), reverse = True)

#     prev = sorted_candi_cnt[0]
#     if prev[1]>0:
#         answers.append(prev[0])
        
#     # 주문 수가 가장 많은 조합들을 answers 에 저장 
#     for sc in sorted_candi_cnt[1:]:
#         if len(sc[0]) != len(prev[0]):
#             prev = sc
#         if sc[1] == prev[1] and sc[1] > 0:
#             answers.append(sc[0])

#     # 각 조합을 가지고 문자열로 변환
#     tmp = []
#     for i in range(len(answers)):
#         answers[i] = sorted(answers[i])
#         tmp.append(''.join(map(str, answers[i])))
        
#     # 중복 문자열 제거
#     set_answer = set(tmp)

#     #  answer 에 저장 
#     for a in set_answer:
#         answer.append(a)
#     # answer 사전순 정렬
#     answer.sort()
#     return answer