

def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        day = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            day += 1
        days.append(day)
    while days:
        cnt = 1
        day = days.pop(0)
        while days and day >= days[0]:
            cnt += 1
            days.pop(0)
        answer.append(cnt)
    return answer

# 모르겠어요... ㅠㅠ