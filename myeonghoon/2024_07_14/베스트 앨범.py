# 8시 15분에 시작

def solution(genres, plays):
    answer = []
    dict = {}
    dict_index = {}
    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]] += plays[i]
            dict_index[genres[i]].append((i, plays[i]))
        else:
            dict[genres[i]] = plays[i]
            dict_index[genres[i]] = [(i, plays[i])]


    sort_test = sorted(dict_index, key = lambda x: dict[x], reverse=True)

    for i in sort_test:
        t= sorted(dict_index[i], key= lambda x: (x[1], -x[0]), reverse=True)[0:2]
        
        for j in t:
            answer.append(j[0])    

    return answer



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# genres순회하면서 classic이면 classic리스트에 넣고 (genres[0], plays[0])
# pop이면 pop 리스트에 넣고 
# genres에 classic 리스트를 만들었는데 그 다음게 classic이 아니면 어떡해?
# 장르가 뭐가 있는 지 모르는 상태잖아?
# 처음 나오는 녀석은 무조건 변수에 저장할까?
# genres 순회하면서 어떻게 골라담지?
# 2번 순회하는 건 좀 그렇잖아...
# list["classic"] = 총합
# list["classic"]= [0, 150], [3, 250]
# classic과 pop 중에 누가 더 클까요?
# pop, classic으로 정렬
# pop = 4, 2500 / 1, 600 and classic 3, 800 / 0, 500 / 2, 150
# index가 아니라 index랑 매칭된 값으로 정렬을 해야 됨.


what_genres = []  
for pair in zip(genres, plays):
    if pair[0] not in what_genres:
        what_genres.append(pair[0])


# for i in range(len(genres)):
#     for j in range(len(what_genres)):
#         if genres[i] == what_genres[j]:
#             dict[what_genres[j]]


    # for j in dict_index[i]:
    #     print(j)



# print(sort_test)
# print(dict)
# print(dict_index)
print(solution(genres=genres, plays=plays))

