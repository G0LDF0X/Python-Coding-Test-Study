import sys

n = int(sys.stdin.readline().strip())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

print(fibonacci(n))


#변수 두 개 만으로 피보나치 수열

import sys

n = int(sys.stdin.readline().strip())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

print(fibonacci(n))