# 1~n까지 n개의 벽이 있다.
# 그중 몇 개의 벽은 페인트를 다시 칠해야한다.
# 롤러의 길이는 m미터이다.
# 롤러는 벽을 벗어날 수 없다.
# 페인트질을 최소화하는 게 조건!


# 안 칠해진 벽의 번호를 출력해주는 기능
def a():
    for num in section:        
        print(num)
# 안 칠해진 벽의 번호랑 롤러의 길이를 더해주는 기능
def b():
    for num in section:        
        roller_end = (m + num)-1
        print(roller_end)

# 롤러로 벽을 칠할 수 있는 범위를 출력해주는 기능
def c():
    for num in section:
        roller_start = num       
        roller_end = (m + num)-1
        print(roller_start, roller_end)

# 리스트에서 롤러의 범위 안에 들어가는 지 확인하는 기능
def d():
    for check in section:
        if roller_start <= check and roller_end >= check:
            print(check)

# 리스트에서 숫자를 빼는 기능
# section.remove(check)

# 롤러를 사용할 때마다 result에 1씩 추가해주는 기능

# 롤러가 1보다 작거나 n보다 크면 알려주는 기능

def solution(n, m, section):
    answer = 0    
    while section:      
        roller_start = section[0]       
        roller_end = (m + roller_start)-1

        if roller_end > n:
            over = roller_end - n # 무조건 양수
            roller_start -= over
            roller_end -= over
        print("롤러: ", roller_start, "부터", roller_end, "까지")
        
        for check in section[:]:
            if roller_start <= check <= roller_end:
                section.remove(check)                
                print("제거된 섹션:", check)

        answer += 1
        print("페인트 칠 횟수 : ", answer)             
        
    return answer


# 어떻게 시간을 줄일까?

# section.remove(check)를 사용하는 대신에 앞에서부터 롤러가 칠한 벽을 제외한 나머지 벽을 칠하는 형식
# 

n = 8 # 벽
m = 4 # 롤러 길이
section = [2, 3, 6] # 페인트 칠해야 되는 벽

print(solution(n, m, section))
print()

n = 5 # 벽
m = 4 # 롤러 길이
section = [1, 3] # 페인트 칠해야 되는 벽

print(solution(n, m, section))
print()

n = 4 # 벽
m = 1 # 롤러 길이
section = [1, 2, 3, 4] # 페인트 칠해야 되는 벽

print(solution(n, m, section))

# 시간 줄이기
# n = 100000 # 벽
# m = 100 # 롤러 길이
# section = list(range(1, 100001, 13)) # 페인트 칠해야 되는 벽

# print(solution(n, m, section))