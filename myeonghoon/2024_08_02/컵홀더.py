# 컵 홀더 문제는 S : 개인석, L : 커플석이 있다.
# 개인석만 존재할 경우 *S*S*S* , 컵홀더의 갯수 = 개인석의 갯수 + 1
# 개인석과 커플석이 같이 있을 경우 *S*LL*S*, 컵홀더의 갯수 = (개인석의 갯수 + 1) - 커플석의 갯수
# 

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
sit = input().strip()



def solution(N, sit):
    answer = 0
    count_ll = 0
    cup_count=0
     
    count_ll += sit.count('LL')

    cup_count = len(sit) +1 - count_ll

    if N <= cup_count:
        return N
    elif N > cup_count:
        return cup_count 


print(solution(N, sit))