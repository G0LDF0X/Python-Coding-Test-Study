import sys 

# 명령의 수 n 입력
n = int(input())

# 스택 초기화
st = []

# n개의 명령 입력 
for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        st.append(int(command[1]))
    elif command[0] == 'pop':
        print(-1) if not st else print(st.pop())
    elif command[0] == 'size':
        print(len(st))
    elif command[0] == 'empty':
        print(1) if not st else print(0)
    elif command[0] == 'top':
        print(-1) if not st else print(st[-1])
    