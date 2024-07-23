# 나무가 필요한 길이 : m
# 나무들의 갯수 : n
# 필요한 나무의 길이 7m
# 정렬하면 10, 15, 17, 20
# h가 낮을 수록 남는 나무의 길의가 길어진다.
# h가 높을 수록 남는 나무의 길이가 짧아진다.
# 최대 길이인 20보다 크면 나무의 길이는 모두 0이 된다.
# 최대 길이인 20에서 절반을 나눈 10에서 출발해보자.
# answer=10이면, 10+5+7 = 22가 된다.
# 실제 h는 7이므로 answer보다 낮다. 오른쪽으로 이동
# h = 10보다 크고 20보다 작다. 10과 20 사이인 h=15이면, 7이 나온다.


# 정렬을 하면 4, 26, 40, 42, 46이다.
# 최대 길이는 46이다. h = 0
# h = 20 은 answer보다 높다. 왼쪽으로 이동. 
# 46에 절반은 answer = 23이다.
# answer =23이면,  42-23=19, 40-23=17, 26-23=3, 46-23=23/ answer는 19+17+3+23 = ?? h는 20이므로 answer보다 작다. 오른쪽으로 이동
# 23 ~ 46 의 절반은 (46+23)/2 = 


def solution(tree, length):
    sort_tree = sorted(tree)
    # 최소, 최대, 중간 길이를 구해야한다.
    max_length = sort_tree[len(sort_tree)-1]
    min_length = 0
    current_length = int((max_length + min_length)/2)

    while True:
        # while문 시작할 때 현재 남은 나무의 길이 초기화
        current_remaining_length = 0

        # 현재 남은 나무의 길이를 구해야 한다.
        # 각 배열을 돌면서 배열의 값이 current_length보다 낮으면 0, 높으면 배열의 값 - current_length
        for i in range(len(sort_tree)):
            if sort_tree[i] <= current_length:
                current_remaining_length += 0
            else:
                current_remaining_length += (sort_tree[i] - current_length)
        
        # 만약 length가 current_remaining_length보다 작다면 길이를 줄이기 위해 오른쪽으로 이동
        if current_remaining_length > length: 
            min_length = current_length
            current_length = int((max_length + min_length)/2)

        # 만약 length가 current_remaining_length보다 크다면 길이를 늘이기 위해 왼쪽으로 이동  
        elif current_remaining_length < length:
            max_length = current_length
            current_length = int((max_length + min_length)/2)

        elif current_remaining_length == length:
            print(current_length)
            break

        elif current_length <= min_length or current_length >= max_length:
            print(max_length)
            break 



tree = [20, 15, 10, 17]
length = 7

solution(tree, length)

tree = [4, 42, 40, 26, 46]
length = 20

solution(tree, length)