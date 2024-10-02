# ["may", "kein", "kain", "radi"]에서 [5, 10, 1, 3]는 19점
# ["may", "kein", "brin", "deny"]에서 may, kein만 있으므로 15점
# ["kon", "kain", "may", "coni"]에서 kain, may만 있으므로 6점

# photo를 돌면서 name에 may, kein, kain, radi가 photo에 있는지 찾는다
# may가 photo에 있으면 may의 idx를 찾아서 yearning의 idx의 값을 sum에 더해준다.
# photo를 다 돌았으면 sum을 answer에 추가해준다.
# photo에 있는 남은 배열이 끝날 때까지 지속한다.

# 이중 루프를 사용하지 않고, photo 리스트의 각 요소를 한 번만 순회하도록 
# 코드를 최적화할 수 있습니다. 이를 위해 name 리스트와 
# yearning 리스트를 딕셔너리로 변환하여 빠르게 점수를 
# 조회할 수 있게 합니다.

# 1. name과 yearning 리스트를 딕셔너리로 변환하여 각 이름에 대한 점수를 빠르게 조회할 수 있게 합니다.
# 2. photo 리스트의 각 그룹을 순회하면서, 각 그룹의 사람들을 한 번만 순회하여 점수를 계산합니다.
# 이렇게 하면 시간 복잡도가 O(n)으로 줄어들어 성능이 향상됩니다.

# i =0, j =0, name = may, 
def solution(name, yearning, photo):
    answer = []
    yearning_dict = {name[i]: yearning[i] for i in range(len(name))}
    
    for i in range(len(photo)):
        sum = 0
        for j in range(len(photo[i])):
            if photo[i][j] in yearning_dict:
                # print(name[j], yearning_dict)
                sum += yearning_dict[photo[i][j]]
        answer.append(sum)
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))

name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]

print(solution(name, yearning, photo))

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may"],["kein", "deny", "may"], ["kon", "coni"]]

print(solution(name, yearning, photo))