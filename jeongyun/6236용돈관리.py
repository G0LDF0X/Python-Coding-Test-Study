import sys

input = sys.stdin.readline

n, m = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))
 
# k가 가능한 범위    
s = max(money)
e = sum(money)

while s<=e :
    mid = (s+e)//2
    withdraw = mid
    cnt = 1
    
    
    for i in money:
        # 인출한 돈이 부족한 경우
        if withdraw <i:
            cnt +=1
            withdraw = mid
        withdraw -=i
    
    
    # 인출횟수가 m 보다 큰 경우
    if cnt > m or mid < max(money):
        s = mid+1
    else:
        e = mid -1
        k = mid
        
print(k)