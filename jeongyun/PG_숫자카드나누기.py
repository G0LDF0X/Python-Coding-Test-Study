from math import gcd
from functools import reduce

# 배열의 최대공약수 구하기 
def get_gcd(arr):
    return reduce(gcd, arr)

def solution(arrayA, arrayB):
    answer = 0
    
    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)
    
    # arrayA의 공약수 중 arrayB를 하나도 나누지 못하는 수 => answer
    for i in range(gcdA, 1,  -1):
        if gcdA % i == 0:
            flagB = True    # arrayB가 arrayA의 공약수로 나누어지는지 확인하기 위한 변수
            for b in arrayB:
                # 만약 arrayB 수 중 나누어지는 수가 있으면 false
                if b % i == 0:
                    flagB = False
            # 모든 arrayB가 안나누어질때 그 수를 answer로 저장 => answer는 최댓값 이므로 max
            if flagB == True:
                answer = max(answer, i)

    # arrayB의 공약수 중 arrayA를 하나도 나누지 못하는 수 => answer
    for i in range(gcdB, 1, -1):
        flagA = True
        if gcdB % i == 0 :
            for a in arrayA:
                if a % i == 0:
                    flagA = False
            if flagA == True:
                answer = max(answer, i)

    return answer