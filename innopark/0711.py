def solution(progresses, speeds):
    answer = []
    days = []
    for progress, speed in zip(progresses, speeds):     #enumerate와 비슷
        days_remaining = ((100 - progress) // speed)
        days.append(days_remaining)
    
    while days:
        current_day = days.pop(0)
        count = 1
        while days and days[0] <= current_day:
            days.pop(0)
            count += 1
        answer.append(count)
    
    return answer


def solution(progresses, speeds):
    answer = []
    days = []
    for progress, speed in zip(progresses, speeds):
        days_remaining = -((progress - 100) // speed)
        days.append(days_remaining)
    
    while days:
        current_day = days.pop(0)
        count = 1
        while days and days[0] <= current_day:
            days.pop(0)
            count += 1
        answer.append(count)
    
    return answer