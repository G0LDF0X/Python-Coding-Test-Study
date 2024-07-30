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
        







#효율적인 코드

import sys
from collections import defaultdict

def max_fruit_length(N, fruits):
    max_length = 0
    start = 0
    fruit_count = defaultdict(int)

    for end in range(N):
        fruit_count[fruits[end]] += 1

        while len(fruit_count) > 2:
            fruit_count[fruits[start]] -= 1
            if fruit_count[fruits[start]] == 0:
                del fruit_count[fruits[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

# 입력 받기
N = int(sys.stdin.readline().strip())
fruits = list(map(int, sys.stdin.readline().strip().split()))

# 결과 출력
print(max_fruit_length(N, fruits))