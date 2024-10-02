# num1 == num2 -> true -> 1
# num1 == num2 -> false -> -1

def solution(num1, num2):
    answer = 0
    if num1 == num2:
        answer = 1        
    else:
        answer = -1
    return answer

num1 = 2
num2 = 3
print(solution(num1, num2))

num1 = 11
num2 = 11
print(solution(num1, num2))

num1 = 7
num2 = 99
print(solution(num1, num2))
