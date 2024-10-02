def solution(n):
    answer = ''
    # 3진수처럼 계산 
    while n >0:
        # 3으로 나눴을때 나머지가 1이면 1
        if n % 3 == 1:
            answer+='1'
            n //=3
        # 3으로 나눴을 때 나머지가 2이면 2
        elif n % 3 == 2:
            answer += '2'
            n //=3
        # 3으로 나눴을 때 나머지가 0이면 4, 몫 -1
        else:
            n //= 3 
            n -=1
            answer += '4'
    
    # 뒤에서 부터 적어야하므로 reverse
    return ''.join(reversed(answer))