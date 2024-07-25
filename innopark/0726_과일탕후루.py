import sys

# 선배님 마라탕 사주세요
# 탕후루도 같이 ?

n= int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().strip().split()))

set_l = set(list)
set_list = list(set_l)

if len(set_list) == 1:
    print(len(list))
    
elif len(set_list) == 2:
    print(len(list))

else:
    while len(set_list) >= 3:
        list.pop(0)
        set_l = set(list)
        set_list = list(set_l)
        if len(set_list) <= 2:
            print(len(list))
            break
        else:
            list.pop(-1)
            set_l = set(list)
            set_list = list(set_l)
            if len(set_list) <= 2:
                print(len(list))
                break
        