import re

def solution(files):
    file_data = []
    index = 0
    
    for file in files:
        head = []
        number = []
        tail = []
        is_number_find = False
        for c in file:
            try:
                c = int(c)
                is_number_find = True
                number.append(str(c))
            except:
                if not is_number_find:
                    if c.isalpha():
                        head.append(c.lower())
                    else:
                        head.append(c)
                else:
                    if c.isalpha():
                        tail.append(c.lower())
                    else:
                        tail.append(c)
        final_head = ''.join(head)
        final_number = int(''.join(number))
        final_tail = ''.join(tail)
        
        file_data.append([final_head, final_number, final_tail, index])
        index += 1

    result = sorted(file_data, key=lambda x: (x[0], x[1], x[2]))
    
    answer = []
    for i in range(len(result)):
        answer.append(files[result[i][3]])
    return answer