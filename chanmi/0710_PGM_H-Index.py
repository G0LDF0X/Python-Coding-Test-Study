def solution(citations):
    # 조건
    # 1 <= n <= 1000 (리스트의 길이는 최대 1000)
    # 0 <= h <= 10000 (리스트 안의 원소는 최대 10000)

    # ciatations를 정렬하여 인덱스의 값과 리스트의 길이를 비교하면 될 것 같다.
    citations.sort()
    h_value = 0
    index = 0

    # index가 리스트의 끝까지 가면 종료
    while index != len(citations) - 1:
        # 현재 비교하고자 하는 h의 값과 citations[index]의 값을 비교했을 때,
        # citations[index]가 h보다 작으면 index를 1 증가시킨다.
        # 예를 들어, h=2인데 citations[index]가 1이면 citatiosn[index]가 h보다 작으므로 index를 1 증가시킨다.
        # 그 이후 값을 확인하여 citations[index]가 h의 값보다 크거나 같을 때까지(예시에서는 2 이상이 될 때까지) index를 증가시킨다.
        while citations[index] < h_value:
            if citations[index] < h_value:
                index += 1
            # 이때, index가 리스트의 끝까지 가면 (예를 들어 [0, 0, 0, 0, 0]이 들어오는 경우)
            # while문을 종료시킨다.
            if index == len(citations) - 1:
                break

        # index를 증가시켰으면, h의 값과 그 이상인 리스트의 길이를 비교하여
        # h 이상인 원소의 개수가 h개 이상이면, h를 1 증가시킨다.
        if len(citations) - index >= h_value:
            h_value += 1
        else:
            return h_value - 1
    return 0
solution([3, 0, 6, 1, 5]) # 3
# [3, 0, 6, 1, 5]의 경우 발표한 논문 수 n은 5고,
# h번을 찾기 위해 카운트하면 아래와 같다.

# h=0인 경우
# 0번 이상 인용된 논문은 5개다. (5 >= 0)

# h=1인 경우
# 1번 이상 인용된 논문은 4개다. (4 >= 1)

# h=2인 경우
# 2번 이상 인용된 논문은 3개다. (3 >= 2)

# h=3인 경우
# 3번 이상 인용된 논문은 3개다. (3 >= 3)

# h=4인 경우
# 4번 이상 인용된 논문은 2개다. (2 < 4) <= 조건 틀림

# 이므로 h의 최댓값은 3이라는 걸 알 수 있다.