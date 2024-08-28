# 예시 1
# x = 10, y = 40, n = 5
# x * 2 = 20, x= 20
# x * 2 = 40, result = 2

# x = 10일 때, x * 3 = 30
# x * 2 = 60(X), x + n = 35 
# x + n = 40
# result = 3

#                              x = 10
#           *2(20),             *3,         +n
# *2(40), *3(60), +n(25)

# 다이나믹 프로그래밍 사용
# 메모이제이션 기법
# *2, *3, +n 3가지 방법 밖에 없다.
# 

def solution(x, y, n):
    answer = 0
    visited = set()

    if (x * 2) < y:
        x = x * 2
        print(x)
        answer += 1
    
    if (x * 3) < y:
        x = x * 3
        print(x)
        answer += 1

    if (x + n) < y:
        x = x + n
        print(x)
        answer += 1

    return answer

print(solution(10, 40, 5))