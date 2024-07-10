from collections import deque
import math
from collections import Counter


# 기능이 100% 일 때 서비스 할 수 있다고 함
# 앞에 있는 기능이 20일 째에 개발 완료되고, 뒤에 있는 기능이 10일 째에 개발이
# 완료된다고 한다면 앞에 있는 기능이 다 개발되고 배포되어야 뒤에 있는 기능도
# 배포할 수 있으므로 2 기능다 20일 째에 배포된다. 
# A = 20일, B = 10(개발완료) -> 20(배포)일

# 만약 작업 진도 = 95% 이고, 작업 속도가 = 4% 이면 1일 째 99%이므로 2일째에 배포가
# 되어져야 한다.



# 큐에 값을 차례대로 넣는다
# 빼고 나서 첫 번 째 수를 임시 저장
# 두 번 째 수를 큐에서 빼고 임시 저장
# 첫 번 째 수와 비교를 해서
# 리스트에 값을 저장

def queue(progresses, speeds):
    answer = []
    queue = deque()
    current = 0
    back = 0

    for i in range(len(progresses)):
        p_remaining = 100 - progresses[i] # 남은 진행률 구하기
        distribution_dt = math.ceil(p_remaining / speeds[i]) # 배포일 올림
        queue.append(distribution_dt) # 배포일을 큐에 넣기

    while queue:
        # 맨 처음에 큐에서 숫자 두개를 빼서 저장
        if current == 0:
            current = queue.popleft()
        else:
            back = queue.popleft()

        if current > back:
            back = current
            answer.append(current)
        else:
            answer.append(back)
        
        current = back 
        #5[0번]을 리스트에 저장
        # 앞쪽으로 7[1번]저장 후 뒤쪽을 큐에서 빼내서 저장
    return answer


def solution(progresses, speeds):
    queue_list = queue(progresses, speeds)

    # 각 원소의 갯수를 세는 Counter 객체 생성
    counter = Counter(queue_list)

    # 결과를 리스트로 변환
    # 각 원소가 등장한 순서대로 리스트에 저장
    result = [counter[num] for num in counter]

    return result


progresses = [93, 30, 55] # [2, 1] 
speeds = [1, 30, 5]
# A 기능 배포일 = 7일
# B 기능 배포일 = 3일
# C 기능 배포일 = 9일

# 7일 A, B 기능 배포
# 9일 C 기능 배포

print(solution(progresses, speeds))

progresses = [95, 90, 99, 99, 80, 99] # [1, 3, 2]
speeds = [1, 1, 1, 1, 1, 1]




# 완전 탐색?

# 0번 기능
# 100 - progresses[0] = 7(남은 진행률)
# 7(남은 진행률) / speeds[0](진행 속도) = 7(배포일)
# 0번 기능 배포일은 7일

# 1번 기능
# 100 - progresses[1] = 70
# 70 / 30 = 2.xxx 반올림해서 3일
# 1번 기능 배포일은 3일

# 0번 기능은 1번 기능 보다 순서가 앞쪽에 있다.
# 0번 < 1번, 숫자가 작은 쪽이 앞쪽
# 앞쪽[0번] = 7일
# 뒤쪽[1번] = 3일
# 큐에서 7을 먼저 빼서 저장
# 뒤쪽 큐에서 3을 빼서 저장
# 만약 7[0번] > 3[1번]이 성립한다면
# 앞쪽 기능의 배포일을 맞춰야 하므로 3[1번]을 7[0번]으로 업뎃
# 7[0번]을 리스트에 저장

# 만약 5[0번] < 7[1번]이 성립한다면
# 5[0번]을 리스트에 저장하고
# 앞쪽을 7[1번]으로 업뎃 



# 2번 기능
# 100 - 55 = 45
# 45 / 5 = 9(큐에 저장)
# 7[1번] > 9[2번] 은 False
# 9[2번]은 그대로 큐에서 빼서 리스트에 저장하면 된다.

