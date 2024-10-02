def solution(n, m, section):
    answer = 0
    i = 0 # 인덱스 위치    
    while i<len(section):      
        roller_start = section[i]        
        roller_end = (m + roller_start)-1

        if roller_end > n:
            over = roller_end - n # 무조건 양수
            roller_start -= over
            roller_end -= over        
        print("롤러: ", roller_start, "부터", roller_end, "까지")
        
        while i<len(section) and roller_start <= section[i] <= roller_end:            
            print("페인드로 덮인 섹션 : ", section[i])
            i += 1               

        answer += 1
        print("페인트 칠 횟수 : ", answer)             
        
    return answer

# 어떻게 시간을 줄일까?

# section.remove(check)를 사용하는 대신에 앞에서부터 롤러가 칠한 벽을 제외한 나머지 벽을 칠하는 형식
# 현재 인덱스의 위치를 출력하는 기능
# 페인트가 칠해지는 범위
# 페인트로 덮히는 섹션

n = 8 # 벽
m = 4 # 롤러 길이
section = [2, 3, 6] # 페인트 칠해야 되는 벽

print(solution(n, m, section))
print()

# n = 5 # 벽
# m = 4 # 롤러 길이
# section = [1, 3] # 페인트 칠해야 되는 벽

# print(solution(n, m, section))
# print()

# n = 4 # 벽
# m = 1 # 롤러 길이
# section = [1, 2, 3, 4] # 페인트 칠해야 되는 벽

# print(solution(n, m, section))