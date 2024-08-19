def solution(x, y, n):
    # x에 n을 더하기
    # x에 2를 곱하기
    # x에 3을 곱하기
    
    # x를 y로 만들기 위한 최소 연산 횟수
    # 2나 3으로 나눌 수 있으면 나누기
    # 안 나눠지면 n을 빼기
    
    current_number = y
    count = 0
    while current_number >= x:
        if current_number == x:
            return count
        
        if current_number - n == x:
            return count + 1
        
        if current_number % 2 == 0:
            current_number //= 2
            count += 1
        elif current_number % 3 == 0:
            current_number //= 3
            count += 1
        else:
            current_number -= n
            count += 1
    return -1