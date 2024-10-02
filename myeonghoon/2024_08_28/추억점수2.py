# 2번 째 방법. 리스트에서 원소를 빼자
# name[0] == photo[0][0] -> true -> total += yearning[0] -> name[0 +1] -> photo[0].pop(0)
# name[1] == photo[0][0] -> true -> total += yearning[1] -> name[1 +1] -> photo[0].pop(0)
# name[2] == photo[0][0] -> true -> total += yearning[2] -> name[2 +1] -> photo[0].pop(0)
# name[3] == photo[0][0] -> true -> total += yearning[3] -> name[3 +1] -> photo[0].pop(0) -> if [3 +1] > len(name)-1 -> true -> name[0], photo[0 +1][0], answer.append(total), total = 0
# name[0] == photo[1][0] -> true -> total += yearning[0] -> name[0 +1] -> photo[1].pop(0)
# 생략
# name[2] == photo[1][0] -> false -> photo[1][0 +1]
# name[2] == photo[1][0] -> false -> photo[1][1 +1] -> if [1 +1] > len(photo[1]) -1 -> true -> photo[1 +1][0]

# def solution(name, yearning, photo):
#     answer = []
#     photo_1arr = 0
#     for j in range(len(photo)):
#         total = 0
#         i = 0
#         # for i in range(len(name)):
#         while True:
#             if name[i] == photo[j][photo_1arr]:
#                 total += yearning[i]
#                 photo[j].pop(photo_1arr)
#                 i += 1

#                 if i > len(name)-1:
#                     answer.append(total)
#                     break
#             else:
#                 photo_1arr += 1
#                 if photo_1arr > len(photo[j]) -1:
#                     photo_1arr = 0
#                     break               
        
#     return answer


def solution(name, yearning, photo):
    answer = []
    name_dict = dict(zip(name, yearning))
    
    for p in photo:
        total = 0
        for person in p:
            if person in name_dict:
                total += name_dict[person]
        answer.append(total)
    
    return answer


# 예제 1
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))

# 예제 2
name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]

print(solution(name, yearning, photo))

# 예제 3
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may"],["kein", "deny", "may"], ["kon", "coni"]]

print(solution(name, yearning, photo))