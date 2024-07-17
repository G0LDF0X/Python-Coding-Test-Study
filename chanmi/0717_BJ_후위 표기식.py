import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 우선순위
# 1. 괄호
# 2. 곱셉 나눗셈(왼쪽에서부터)
# 3. 덧셈 뺼셈(왼쪽에서부터)

(A + B) * C
((A * C) + B) / D

notation = input().strip()

bracket_stack = []
answer = ""

# 괄호 찾기 -> 괄호의 처리가 이번 문제 풀이의 핵심
# 괄호가 한 번 열렸다가 닫힐 때까지 전부 스택에 넣고 닫히면 스택을 전부 빼서 합치기?
for no in notation:
    # 알파벳인 경우에는 그냥 넣기
    if no.isalpha():
        answer += no

    # 문장부호인 경우
    else:
        if no == "(":
            bracket_stack.append(no)
        elif no == ")":
            bracket_stack.pop()
        elif no == "+" or no == "-":
            # (가 스택에 없이 그냥 더하는 경우
                pass
        elif no == "*" or no == "/":
            pass