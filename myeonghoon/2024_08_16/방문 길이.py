# U : (0, 1) D: (0, -1) R: (1, 0) L : (-1, 0)
# 처음 걸어본 길이 구하기
# (5, 5), (-5, 5), (5, -5), (-5, -5) 보드 크기
# "ULURRDLLU" -> posi[0] + U[0], posi[1]+ U[1] ... 
# 0, 0의 위치는 visit = 1(방문 완료)
# visit == 1이면 count 값 증가 없음
# 현재 위치가 보드 크기에서 벗어나면 위치 변경 없음

# U가 들어오면 x는 +0, y는 +1 더해주기
# 보드판 만들기
# 0,0 은 이미 방문했으므로 1로 변경
# 위치 이동하면서 방문된 곳은 방문 완료로 변경
# count 값 +1씩 증가
# visit이 1이면 count 값 증가 없음.

# 오류 지나간 적어 없는 길이라도 도착지점이 방문완료 상태면 count값이 증가하지 않는다.
# 해결 방법? 시작 지점이 0일 경우 count값 증가?

# 현재 위치가 -5나 +5를 넘는다면// 위치이동 x count 값 증가 x

def solution(dirs):
    answer = 0
    current_position = [0, 0]

    # 11 * 11 보드판
    board_size = 11
    visit = [[0 for _ in range(board_size)] for _ in range(board_size)]
    offset = 5

    # 0,0을 방문 완료 상태로 변경
    # visit[0+offset][0+offset] = 1     

    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]        

    for i in dirs:
        next_position = current_position[:]
        if i == 'U':
            next_position[0] += x[0]
            next_position[1] += y[0]
        elif i == 'D':
            next_position[0] += x[1]
            next_position[1] += y[1]
        elif i == 'R':
            next_position[0] += x[2]
            next_position[1] += y[2]
        elif i == 'L':
            next_position[0] += x[3]
            next_position[1] += y[3]

        # 현재 위치가 보드 크기에서 벗어나면 위치 변경 없음
        if next_position[0]+offset > 10 or next_position[0]+offset < 0 or next_position[1]+offset > 10 or next_position[1]+offset < 0:
            continue

        if visit[current_position[0]+offset][current_position[1]+offset] == 0:
            answer += 1 
            visit[current_position[0]+offset][current_position[1]+offset] = 1

        current_position = next_position


    # for row in visit:
    #     print(row)          

    return answer


def solution2(dirs):
    answer = 0

    path = set()
    x, y = 0, 0 

    for direction in dirs: 
        if direction == "U":
            if y + 1 <= 5:
                new_y = y + 1
                path.add(((x, y), (x, new_y)))
                path.add(((x, new_y), (x, y)))
                y = new_y

        elif direction == "D":
            if y - 1 >= -5:
                new_y = y - 1
                path.add(((x, y), (x, new_y)))
                path.add(((x, new_y), (x, y)))
                y = new_y

        elif direction == "R":
            if x + 1 <= 5:
                new_x = x + 1
                path.add(((x, y), (new_x, y)))
                path.add(((new_x, y), (x, y)))
                x = new_x

        elif direction == "L":
            if x - 1 >= -5:
                new_x = x - 1
                path.add(((x, y), (new_x, y)))
                path.add(((new_x, y), (x, y)))
                x = new_x

    answer = len(path) // 2

    return answer


dirs = "ULURRDLLU"
print(solution2(dirs))

dirs = "LULLLLLLU"
print(solution2(dirs)) # 9