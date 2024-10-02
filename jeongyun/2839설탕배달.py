import sys

input = sys.stdin.readline

n = int(input())
ans = 0

# 5의 배수가 남을때까지 3 만 가능
while n % 5 != 0 and n >=0:
    n -=3
    ans +=1
if n <0:
    ans = -1
    
# 남은 5의 배수는 5로 나눈 몫으로 계산
if  n % 5 == 0:
    ans += (n // 5)
        
print(ans)

#