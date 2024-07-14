def solution(s):
    new_list=[]
    for i in s.split("},"): # 뒷 괄호 기준으로 덩어리씩 분리
        new_list.append(i.replace("{","").replace("}","").split(",")) # 중괄호 지우고 요소 하나하나 나눠서 리스트에 넣기
    new_list.sort(key=len) # 개수 기준 오름차순 정렬
    answer=[]
    for i in new_list:
        for j in i:
            if j not in answer:
                answer.append(j) # 앞에서부터 새롭게 나오는 요소 순으로 넣음
    return list(map(int,answer))