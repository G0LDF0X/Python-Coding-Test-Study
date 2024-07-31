import sys
import re

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

expressions = input().strip()

# 55 - 50 + 40의 경우,
# 55 - (50 + 40)으로 괄호를 치면 -35가 나온다.

# 그렇지만 만약 빼기가 두 개 이상 나오는 경우,
# 예를 들어 55 - 50 + 40 - 10 + 20의 경우,
# 55 - (50 + 40) - (10 + 20)이 최소의 결과를 만든다.
# 즉, 빼기가 나오면 그 다음 빼기가 나올 때까지 괄호를 치면 된다.

# 다시 말해 빼기를 기준으로 split하고, 내부의 연산을 수행한 뒤 0번째 인덱스의 값에서 이후의 값들을 뺴주면 된다.
# 이때, 인덱스 안에는 40+50과 같은 값들이 들어가므로 해당 값들을 연산하기 위해 리스트 안에서 다시 + 괄호를 기준으로 split 해준다.

split_expressions = expressions.split('-')

for i in range(len(split_expressions)):
    plus_split = split_expressions[i].split('+')
    split_expressions[i] = sum(map(int, plus_split))

result = int(split_expressions[0]) - sum(split_expressions[1:])
print(result)