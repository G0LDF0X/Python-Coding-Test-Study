import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ans = 1
# 1번 연산 a * 2 
# 2번 연산 a * 10 + 1

while a < b :
    # b 가 홀수이면 마지막 연산은 무조건 2번
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:       # 이 else 조건을 안붙이면 시간 초과 .. 
        break
    ans +=1

if a==b:
    print(ans)
else:
    print(-1)