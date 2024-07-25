import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())

promise_list = []

# 풀이 참조 : 기다리는 시간의 중간값을 사용.
# 홀수일 경우에는 중간값이 하나이므로 1
# 짝수일 경우에는 중간값이 2개가 나오므로 그 둘을 뺀값 + 1이라고 함

# 우리는 SUM(ABS(Ai - Bi + T))의 최소값을 구하는 것인데,
# 이때 해당 값을 최소로 만드는 T는 T = Ai - Bi이다.
# 참고한 링크 : https://iamneveralone.tistory.com/50


for i in range(N):
    A, B = map(int, input().split())
    # 기다리는 시간을 append 함
    promise_list.append(A - B)

promise_list.sort()
promise_len = len(promise_list)

# 홀수일 경우
if promise_len % 2 == 1:
    print(1)

# 짝수일 경우
else:
    print(abs(promise_list[promise_len // 2] - promise_list[promise_len // 2 - 1]) + 1)