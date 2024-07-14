import string
from collections import deque

def solution(priorities, location):
    answer = 0
    return answer


def key_value(priorities):
    # 알파벳 키 리스트 생성
    keys = list(string.ascii_lowercase[:len(priorities)])

    # 리스트와 키를 매핑하여 사전 생성
    mapped_dict = dict(zip(keys, priorities))

    return mapped_dict


def test_1(priorities, location):
    answer = 0
    key = priorities[location]

    priorities_queue = deque(priorities)

    while priorities_queue:
        action = True
        queue_st = priorities_queue.popleft()

        for i in range(len(priorities)): # priorities 전체 조회
            if queue_st < priorities[i]: # 한 번이라도 True가 뜨면
                priorities_queue.append(queue_st) # 임시 저장소에 저장되어 있던 값을 다시 큐에 저장하기
                action = False
                break
        
        if action == True: # 만약 
            answer += 1
            if queue_st == key:
                return answer        


# priorities = [2, 1, 3, 2]
# location = 2

# print(test_1(priorities, location)) 

priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(test_1(priorities, location))
 
# 답은 1
# 첫번 째 시도 : 3

# 완전 탐색

# priorities 각 원소마다 우선순위가 있다.
# location 은 해당 원소가 몇 번 째로 실행되는지 구하면 된다.
#  1 ~ 100
# location = 2
# answer = 1

# index[0]을 뽑는다. data = 2
# priorities = [1, 3, 2]
# 2 < 1 False
# 2 < 3 True
# 2를 다시 큐에 집어 넣는다 (큐를 전부 뒤졌는데 True가 없으면 실행)
# priorities = [1, 3, 2, 2]

# index[0]을 뽑는다. data = 1
# priorities = [3, 2, 2]
# 1 < 3 True
# 1을 다시 큐에 넣는다(뒤에)
# priorities = [3, 2, 2, 1]

# index[0]을 뽑는다. data = 3
# priorities = [2, 2, 1]
# 3 < 2 False[1]
# 3 < 2 False[2]
# 3 < 1 False[3] 모든 큐를 조회했는데 모두 False
# answer 값을 1 증가시키고
# data 키랑 location키랑 비교해서 같으면
# answer 반환하고 종료 

# 순서를 지켰다??

# 실패한 상태는 임시 저장이 된 값보다 큰 값(우선순위가 높은)값이 큐에 들어있을 때
# 성공한 상태는 큐를 모두 돌았을 때 임시 저장된 값보다 큰 값이 없는 경우