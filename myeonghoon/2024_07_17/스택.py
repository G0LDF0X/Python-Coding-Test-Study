# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# push 1의 경우에 push는 str 1은 int 형일 것이라고 예상
# push를 입력할 경우 정수를 입력할 수 있도록 하는 것이 맞지 않을까?
# 스택은 먼저 들어온 값이 맨 밑에 쌓인다.
# 스택에서 값을 뽑을 때는 가장 최근에 들어온 값이 출력되어야 한다.
# 

def test_1(n):    
    stack = []
    for _ in range(n):
        stack_input = str(input())

        if stack_input == 'push':
            x = int(input())
            stack.append(x)
            print(stack)
        elif stack_input == 'pop':        
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif stack_input == 'size':
            print(len(stack))
        elif stack_input == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif stack_input == 'top':
            if stack:
                print(stack[len(stack)-1])
            else:
                print(-1)


n = int(input())

test_1(n)

    




