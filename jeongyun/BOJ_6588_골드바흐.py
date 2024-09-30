import sys
from math import sqrt
input = sys.stdin.readline

def is_prime_2(n):
    arr = [True]*(n+1)
    
    for i in range(2, int(sqrt(n))+1):
        if arr[i] == True:
            for j in range(i*i, n+1, i):
                arr[j]=False
    return arr
    
arr = is_prime_2(1000001)

while True:
    n = int(input())
    
    if n == 0:
        break
    
    ans = []
    
    x = n//2 +1
    
    for i in range(3, x, 2):
        if arr[i] and arr[n-i]:
            ans.append(i)
            ans.append(n-i)
            break

    if len(ans)==0:
        print("Goldbach's conjecture is wrong.")
    ans.sort()
    print(n, '=', ans[0], '+', ans[1])
    