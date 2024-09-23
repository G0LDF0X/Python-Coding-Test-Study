import sys
from math import sqrt, ceil
input = sys.stdin.readline


def is_prime(x, primes):
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(x)) + 1):
        if primes[i]:
            for j in range(i * i, x + 1, i):
                primes[j] = False
    return primes
    
            
primes = [True] * (123456*2+1)
is_prime(123456*2, primes)

while True:
    n = int(input())
    ans = 0
    if n == 0:
        break
    
    for x in range(n+1, 2*n + 1):
        if primes[x]:
            ans+=1
    print(ans)

# 시간 초과 풀이 
# def is_prime(x):
#     for i in range(2, int(sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True

# while True:
#     n = int(input())
#     ans = 0
#     if n == 0:
#         break
    
#     for x in range(n+1, 2*n + 1):
#         if is_prime(x):
#             ans += 1
#     print(ans)
