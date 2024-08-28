# 예시 1번
# numbers = 2, 3, 3, 5
# 현재 위치가 2일 때 2보다 위치상으로 뒤에 있고, 큰 숫자는 3, 5가 있음
# 3이 5보다 위치상으로 앞에 있기 때문에 3
# 위치를 한 칸 뒤로 옮기면 3, 3보다 뒤에 있는 숫자는 3, 5
# 그 중에 3보다 큰 숫자는 5
# 위치를 한 차례 뒤로 옮기면 3, 뒤는 마찬가지
# 위치를 한 차례 뒤로 옮기면 5, 5보다 뒤에 있는 숫자는 없으므로 -1

# 프로그래밍 순서
# list 2, 3, 3, 5
# 현재 위치를 가리키는 변수를 만든다.
# 2보다 뒤에 있는 배열을 순차적으로 접근
# 2보다 큰 숫자 찾기
# 바로 뒤에 있는 숫자 찾기
# n+1 값이 존재하지 않는 경우 for문은 실행하지 않는다 -> 임시 변수를 만들어서 0으로 초기화하면 for 문이 실행하지 않아도 값이 없다는 것을 알 수 있음.


# 현재 위치가 0일 때 1~3
# 현재 위치가 1일 때 2~3
# 현재 위치가 2일 때 3
# 현재 위치가 3일 때 -1

# 2 -> 3, 3, 5
# 3 -> 3, 5
# 3 -> 5
# 5 -> x

# [9, 1, 5, 3, 6, 2]
# 9 -> 1, 5, 3, 6, 2 (5번) => 9 뒤에 배열을 정렬하면 6, 5, 3, 2, 1 (1번), 가장 큰 수인 6이랑만 비교하면 됨.
# 1 -> 5, 3, 6, 2 (4번) => 6, 5, 3, 2 => 
# 만약 2 -> 111111111131115일 때 3을 가장 빠르게 찾을 수 있는 방법은?
# 가장 가까이에 있는? 현재 위치가 0 가장 가까이에 있는 위치는 1이다. 
# 어떻게 스택이 더 빠른 지 이해가 되지 않는다....
# n

# 출력 크기 초과
def solution(numbers):
    answer = []
    
    
    for current in range(len(numbers)):
        answer_value = 0
        print(numbers[current])        
        for i in range(current+1, len(numbers)):                            
            if numbers[current] < numbers[i]:
                answer_value = numbers[i]                             
                answer.append(answer_value)
                break
        if answer_value == 0:
            answer.append(-1)               

    return answer

numbers = [2, 3, 3, 5]
print(solution(numbers))

numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))