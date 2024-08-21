from math import comb

def solution(n):
    # 세로 길이가 2이고, 가로 길이가 n인 바닥을 채우려고 함.
    
    # 직사각형을 세로로 놓는 경우는 가로 1, 높이 2
    # 직사각형을 가로로 놓는 경우에는 총 두 개를 놓아서 가로2 세로 2로 만들음
    
    # 이 사각형을 채울 수 있는 경우의 수 찾기
    
    # 먼저 가로 2짜리를 다 채운 다음에 가로 1을 채우는 방법
    # 가로 2짜리는 세로 2짜리로도 변경 가능함.
    
    # 그리고 가로 2짜리를 하나씩 줄여가면서 개수 세기
    
    max_2_count = n // 2
    answer = 0
    
    for i in range(max_2_count, -1, -1):
        width_2_count = i
        width_1_count = n - 2 * i
        answer += comb(width_1_count + width_2_count, width_2_count)
    
    
    return answer

print(solution(4)) # 5