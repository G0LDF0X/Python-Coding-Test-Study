import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

while True:
    command = input().rstrip()
    if command == '0':
        break

    tmp_list = command.split()
    N = int(tmp_list[0])
    numbers = list(map(int, tmp_list[1:]))
    numbers.sort()
    list_len = len(numbers)

    number_list = deque(numbers)
    zero_list = []
    first_number = []
    second_number = []

    turn_count = 0 # 0이면 first_number에 넣을 차례, 1이면 second_number에 넣을 차례

    while number_list or zero_list:
        if len(number_list) > 0 and number_list[0] == 0:
            # 둘다 가장 앞자리인 경우
            if first_number == [] or second_number == []:
                zero_list.append(number_list.popleft())
                continue

            # 둘 다 채워져 있는 경우
            else:
                if turn_count == 0:
                    first_number.append(number_list.popleft())
                    turn_count = 1
                else:
                    second_number.append(number_list.popleft())
                    turn_count = 0
        elif len(zero_list) != 0 and (first_number != [] and second_number != []):
            if turn_count == 0:
                first_number.append(zero_list.pop())
                turn_count = 1
            else:
                second_number.append(zero_list.pop())
                turn_count = 0
        else:
            if turn_count == 0:
                first_number.append(number_list.popleft())
                turn_count = 1
            else:
                second_number.append(number_list.popleft())
                turn_count = 0
    
    first_number_int = int(''.join(map(str, first_number)))
    second_number_int = int(''.join(map(str, second_number)))
    print(first_number_int + second_number_int)
            

# 길이가 홀수라면, 가장 큰 자리에 가장 작은 숫자(0 제외)를 넣고, 그 다음부터 차례로 하나씩 넣으면 해결