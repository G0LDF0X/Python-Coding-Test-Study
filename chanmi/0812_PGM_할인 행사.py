def solution(want, number, discount):
    fruit_dict = {}
    count = 0
    for i in range(len(want)):
        fruit_dict[want[i]] = number[i]
    
    for i in range(len(discount) - 9):
        is_same = True
        check_list = discount[i:i+10]
        for fruit in want:
            if check_list.count(fruit) == fruit_dict[fruit]:
                continue
            else:
                is_same = False
        
        if is_same:
            count += 1
    return count