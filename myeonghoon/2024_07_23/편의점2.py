# |x1-x2|+|y1-y2|?
# 모든 고객들의 거리 합을 최소로 하는 위치에 편의점을 세울 때
# n = 5 
# 2 2
# 3 4
# 5 6 
# 1 9
# -2 -8

# [x1, y1] = [2, 2], [x2, y2] = [3, 4], [x3, y3] = [5, 6], [x4, y4] = [1, 9], [x5, y5] = [-2, -8]
# x = [-2, 1, 2, 3, 5]
# y = [-8, 2, 4, 6, 9]
# [-2, -8]는 [1, 2]지점과의 거리가 제일 짧다. 길이 13
# [1, 2]와 가까운 지점은 [2, 4]이다. 거리 3
# [2, 4]와 가까운 지점은 [1, 2] 거리 3 / [3, 6] 거리 3
# [3, 6]와 가까운 지점은 [2, 4] 거리 3
# [5, 9]와 가까운 지점은 [3, 6] 거리 5
# 만약 [2, 4]에 편의점을 세울 경우 [-2, -8] 거리 16, [1, 2] 거리 3, [3, 6] 거리 3, [5, 9] 거리 8 / 총 16+3+3+8 = 30
# 만약 [1, 2]에 편의점을 세울 경우 [-2, -8] 거리 13, [2, 4] 거리 3, [3, 6] 거리 6, [5, 9] 거리 11 / 총 13+3+6+11 = 33
# 만약 [3, 6]에 편의점을 세울 경우 [-2, -8] 거리 19, [1, 2] 거리 6, [2, 4] 거리 3, [5, 9] 거리 대충 2보다 큼.
# [2, 4]에 세워야 가장 거리가 짧다.

# [2, 4]는 배열의 가운데 지점이다.


def solution(x, y):
    answer = 0
    # x, y를 작은 순에서 큰 순으로 정렬해야 함
    sort_x = sorted(x)
    sort_y = sorted(y)   

    convenience_store_location_x = sort_x[int(len(sort_x)/2)]
    convenience_store_location_y = sort_y[int(len(sort_y)/2)]

    # x의 가운데 값과 y의 가운데 값 출력
    convenience_store_location = [convenience_store_location_x, convenience_store_location_y]

    # 배열에 있는 모든 좌표와 편의점 위치의 거리를 계산해서 모두 더해줘야 한다.
    for i in range(len(x)):
        answer += absolute_value(sort_x[i], convenience_store_location[0]) + absolute_value(sort_y[i], convenience_store_location[1]) 
    
    return answer


def absolute_value(x, y):
    if (x-y) >= 0:
        return x-y
    elif (x-y) < 0:
        return -(x-y)

x = [2, 3, 5, 1, -2]
y = [2, 4, 6, 9, -8]

print(solution(x, y))
