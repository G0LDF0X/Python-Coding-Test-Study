# a b c 있고, 3개의 숫자가 다르다면 
# abc가 모두 같은 경우
# abc 중에 2개만 같은 경우 ab/c a/bc b/ac
# abc 중에 3개 다 다른 경우

# 각 경우에 따라서 경우 1, 경우 2, 경우 3으로 나눈다.
# 주사위 값은 a, b, c 각각 1-6이므로 랜덤 값 지정
# abc의 각 경우에 따라서 결과값 출력

def solution(a, b, c):
    answer = 0
    
    if a == b and b == c and c == a:
        answer = (a+ b+ c) * (a**2+b**2+c**2) * (a**3 + b**3 + c**3)

    elif a == b or b == c or c == a:
        answer = (a+ b+ c) * (a**2+b**2+c**2)

    else:
        answer = (a+ b+ c)

    return answer


a = 2
b = 6
c = 1
print(solution(a, b, c))

a = 5
b = 3
c = 3
print(solution(a, b, c))

a = 4
b = 4
c = 4
print(solution(a, b, c))