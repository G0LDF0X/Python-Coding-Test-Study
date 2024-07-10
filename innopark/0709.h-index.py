def solution(citations):
    answer = 0
    citations.sort(reverse = True) # 내림차순으로 정렬
    for num, citation in enumerate(citations):
        # 피 인용수가 논문의 수랑 같아지는 지점(num은 0부터 시작하니까 +1)
        if citation >= num+1: 
            h_index = num+1
            answer = h_index

    return answer