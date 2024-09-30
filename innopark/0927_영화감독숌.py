import sys
input = sys.stdin.readline

N = int(input().strip())

count = 0
num = 666

while True:
    if '666' in str(num):
        count += 1
        if count == N:
            print(num)
            break
    num += 1