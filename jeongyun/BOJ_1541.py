import sys
input = sys.stdin.readline

arr = input()

operand = []
operator = []

tmp = 0

# 계산의 기본은 앞에서부터 계산, 괄호가 있으면 그것부터 계산 
# 모든 경우를 다 해보고 최솟값 찾자 
# 스택을 가지고 길이가 3 이면 다 빼서 계산한 후에 다시 push 
st = []
for i in range(len(arr)):
    print(st)

    if arr[i] == '+' or arr[i] == '-':
        st.append(int(arr[tmp:i]))
        operand.append(int(arr[tmp:i]))
        tmp = i+1
        if len(st) >= 3:
            a = st[0]
            b = st[2]
            op = st[1]
            st=st[3:]
            if op == '+':
                st.append(a+b)
            elif op == '-':
                st.append(a-b)
        st.append(arr[i])
        operator.append(arr[i])
    
st.append(int(arr[tmp:]))    
if len(st) == 3:
        a = st[0]
        b = st[2]
        op = st[1]
        
        st=[]
        if op == '+':
            st.append(a+b)
        elif op == '-':
            st.append(a-b)
print(operand, operator, st)
        
