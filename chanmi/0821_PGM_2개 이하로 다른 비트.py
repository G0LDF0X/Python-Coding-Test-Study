def solution(numbers):
    # 10의 15승을 2진수로 나타내면 엄청나게 커진다.
    # 완탐은 무리일듯...
    
    # 뒤에 0이 있을 경우 가장 뒤에 오는 0에 1을 넣기
    # 만약 뒤에 0이 없을 경우, 맨 앞에 1을 넣고 바로 뒤에 0 넣기
    answer = []
    
    for number in numbers:
        binary_value = format(number, 'b')
        binary_list = list(binary_value)
        
        if '0' in binary_list:
            for i in range(len(binary_list) - 1, -1, -1):
                if binary_list[i] == '0':
                    binary_list[i] = '1'
                    # 1~2개 이하로 다르면 되기 때문에, 뒤쪽에 있는 0 하나를 1로 바꿨을 경우 바로 그 다음에 있는 1을 0으로 바꿔주면 숫자가 작아지게 된다.
                    if i + 1 < len(binary_list):
                        binary_list[i + 1] = '0'
                    break
        else:
            binary_list.insert(0, '1')
            binary_list[1] = '0'
        
        final_number = int(''.join(binary_list), 2)
        answer.append(final_number)
            
    return answer