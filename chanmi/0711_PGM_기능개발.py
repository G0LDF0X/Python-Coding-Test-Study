from collections import deque

def solution(progresses, speeds):
    remain_days = deque()
    for i in range(len(progresses)):
        # 각 프로세스가 마무리 되기까지 필요한 날들을 계산
        remain_day = (100 - progresses[i]) // speeds[i]
        # 만약 66% 된 일이 하루에 5%씩 작업된다면 34%를 마무리하기 위해 7일이 필요하다.
        # 이를 위해 나머지가 딱 나누어 떨어지지 않을 경우 1을 더해준다.
        if (100 - progresses[i]) % speeds[i] != 0:
            remain_day += 1
        remain_days.append(remain_day)
    
    answer = []

    # 앞에 있는 기능이 개발되어야 전부 배포 가능
    current_days = remain_days[0]
    days_count = 1
    remain_days.popleft()
    while remain_days:
        if remain_days[0] <= current_days:
            days_count += 1
            remain_days.popleft()
        else:
            answer.append(days_count)
            days_count = 0
            current_days = remain_days[0]

    answer.append(days_count)
    return answer

solution([93, 30, 55], [1, 30, 5])