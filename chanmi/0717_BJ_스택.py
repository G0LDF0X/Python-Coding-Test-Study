import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 명령의 수 N (1 <= N <= 10000)
n = int(input())

# 저장할 스택
stack_data = []

for i in range(n):
    command = input().split()

    # push로 시작하는 경우
    if command[0] == 'push':
        stack_data.append(command[1])
    elif command[0] == 'pop':
        if len(stack_data) == 0:
            print(-1)
        else:
            print(stack_data.pop())
    elif command[0] == 'size':
        print(len(stack_data))
    elif command[0] == 'empty':
        if len(stack_data) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack_data) == 0:
            print(-1)
        else:
            print(stack_data[-1])