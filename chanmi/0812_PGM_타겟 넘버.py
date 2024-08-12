count = 0

def dfs(number, answer, target, numbers):
    global count
    if number == len(numbers):
        if answer == target:
            count += 1
        return
    
    dfs(number + 1, answer + numbers[number], target, numbers)
    dfs(number + 1, answer - numbers[number], target, numbers)
    

def solution(numbers, target):
    global count
    count = 0
    dfs(0, 0, target, numbers)
    return count