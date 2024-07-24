import sys
input = sys.stdin.readline

n = int(input())
computer = []

for i in range(n):
    computer.append(list(map(int, input().split())))

for i in range(max(computer)):
    active = 0
    for j in range(n):
        for k in range(n):
            if active >= (n*n) // 2:
                print(i)
                break
            if computer[j][k] <=i:
                active +=computer[j][k]