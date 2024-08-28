# name[0] == photo[0][0] -> true -> total += yearning[0] -> name[0 +1] -> photo[0][0 +1]
# name[1] == photo[0][1] -> true -> total += yearning[1] -> name[1 +1] -> photo[0][1 +1]
# name[2] == photo[0][2] -> true -> total += yearning[2] -> name[2 +1] -> photo[0][2 +1]
# name[3] == photo[0][3] -> true -> total += yearning[3] -> name[3 +1] -> if [3 +1] > len(name)-1 -> true -> name[0], photo[0 +1][0], answer.append(total), total = 0
# name[0] == photo[1][0] -> true -> total += yearning[0] -> name[0 +1] -> photo[0 +1][0 +1]
# 생략
# name[2] == photo[1][2] -> false -> photo[1][2 +1]
# name[2] == photo[1][3] -> false -> photo[1][3 +1] -> if [3 +1] > len(photo[1]) -1 -> true -> photo[1 +1][0]
# 생략
# for ? in range(len(photo)):

def solution(name, yearning, photo):
    answer = []

    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

solution(name, yearning, photo)