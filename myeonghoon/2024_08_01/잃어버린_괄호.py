# 부호는 +와 - 2가지임
# 리스트 안에서 숫자의 위치 이동은 없고 괄호를 부여해 줄 수 있다.
# 앞에서부터 순서대로 계산하면 35
# 괄호의 기능상 맨 앞과 맨 뒤를 계산할 수는 없음
# A 와 B, B와 C 이런 식으로 계산할 수 밖에 없음.
# 특수 문자를 끼고 앞뒤 전후로 나눠야 함.
# 55, -, 50, +, 40 
# - 를 가장 마지막에 계산한다.
# 55 쌓고, -가 들어오면 쌓고, 50 쌓고, + 쌓고, 40쌓고, 숫자 중간에 부호가 + 이면 계산해서 다시 쌓자.
# 

from collections import deque

def solution(list):
    list_deque=deque()
    for i in range(len(list)):
        if list[i] == '-':
            list_deque.append(list[i])
        
        elif list[i] == '+':
            list_deque.pop() 
        
        else:
            list_deque.append(list[i])

        number.append(list[i]) 

list = ['5','5','-','5','0','+','4','0']
print(solution(list))