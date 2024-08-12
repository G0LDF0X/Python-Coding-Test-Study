def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(cur, i):
        nonlocal answer 
        if i >=n:
            if cur == target:
                answer +=1
                return True
            else:
                return False
        dfs(cur+numbers[i], i+1)
        dfs(cur-numbers[i], i+1)
    
    dfs(0,0)
    return answer