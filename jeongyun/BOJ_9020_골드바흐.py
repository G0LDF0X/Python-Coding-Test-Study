import sys
from math import sqrt
input = sys.stdin.readline

def is_prime(x):
    if x <2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i ==0:
            return False
    return True
    
t = int(input())

while t>0 :
    t-=1
    
    n = int(input())
    ans = []
    
    x = n//2 +1
    
    for i in range(x, 1, -1):
        if is_prime(i):
            if is_prime(n-i):
                ans.append(i)
                ans.append(n-i)
                break
            else:
                continue
    ans.sort()
    print(ans[0], ans[1])
    