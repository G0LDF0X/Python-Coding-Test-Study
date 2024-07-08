def solution(people, limit):
    answer = 0
    for _ in range(len(people)):
        if len(people)!=0:
            answer += greedy(people, limit)
    return answer


def greedy(people, limit):
    # 2명이 가능한 지 확인해야 한다.
    # 만약 70부터 시작하면 자기 자신 이외의 숫자를 조회해서 limit(100) - 70 => x <= 30 이여야만 한다.
    # 만약 x가 30이라면 70과 30 둘다 리스트에서 빼고, 보트 +1
    # 만약 그런 숫자가 없다면 보트 +1 하고 리스트에서 70제외
    start = 0
    team_yn = limit - people[start]
    
    for i in range(1, len(people)):
        if people[i] <= team_yn: # i = 1
            people.pop(i)  # i번째 요소 제거
            people.pop(start)
            return int(1)
    people.pop(start)
    return 1
            

people = [70, 50, 80, 50, 150]
print(solution(people, 100))

people = [70, 80, 50]
print(solution(people, 100))