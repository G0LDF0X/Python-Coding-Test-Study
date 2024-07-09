def solution(people, limit):
    answer = 0
    n = len(people)
    l = 0 
    r = n-1
    people.sort(reverse =  True)
    
    while l <= r:
        if people[l] + people[r] <= limit:
            l +=1
            r -=1
        else:
            l +=1
        answer += 1
    return answer