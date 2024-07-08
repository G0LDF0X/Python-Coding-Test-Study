def solution(people, limit):
    people.sort(reverse=True)
    count = 0
    
    # 투 포인터 접근
    start = 0
    end = len(people) - 1
    
    while start <= end:
        # 가장 무거운 사람과 가장 가벼운 사람이 limit보다 작을 경우
        # 둘을 같은 배에 태우고 그 다음으로 무거운 사람과 그 다음으로 가벼운 사람의 무게를 비교해봄
        if people[start] + people[end] <= limit:
            end -= 1
            
        # 만약 가장 무거운 사람과 가장 가벼운 사람이 limit보다 클 경우
        # 가장 무거운 사람은 배를 혼자 타고, 그 다음으로 무거운 사람과 가장 가벼운 사람을 비교함.
        count += 1
        start += 1
    
    return count