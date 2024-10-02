# num -> num % 2 ==0 -> return "Even"
# num -> num % 3 ==0 -> return "Odd"
# 

def solution(num):
    answer = ''

    if num == 0:
        answer += "Even"
    elif num % 2 == 0:
        answer += "Even"
    else:
        answer += "Odd"   
    
    return answer

num = 25
print(solution(num))

num = 4
print(solution(num))

num = 157
print(solution(num))