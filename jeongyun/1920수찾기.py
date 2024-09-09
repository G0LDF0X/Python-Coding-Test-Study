import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()

def findA(x):
    l = 0
    r = n-1
    
    while l <= r:
        m = (l + r) // 2
        if x == a[m]:
            print(1, end='\n')
            break
        elif x < a[m]:
            r = m-1
        elif x > a[m]:
            l = m+1
    if x != a[m]:
        print(0, end='\n')

    
m = int(input())
b = list(map(int, input().split()))

for i in range(m):
    findA(b[i])

