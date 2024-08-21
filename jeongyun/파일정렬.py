def solution(files):
    answer = []
    file_sort = []
    
    for file in files:
        head = ''
        number = ''
        for i in range(len(file)):
            if file[i].isdigit():
                if head == '':
                    head = file[:i]
                number+=file[i]
            if len(number) > 0 and file[i].isdigit() is False:
                break
        file_sort.append([file, head.lower(), int(number)])
        
    # print(file_sort)
    file_sort.sort(key = lambda x : (x[1], x[2]))
    for file in file_sort:
        answer.append(file[0])
    return answer