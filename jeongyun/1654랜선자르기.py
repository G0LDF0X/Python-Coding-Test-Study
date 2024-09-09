import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = []
total = 0

for i in range(k):
    x = int(input())
    line.append(x)
total = sum(line)
    
l = 1   # 가능한 최소 길이 
r = total // n  # 가능한 최대길이 (전체 랜선길이의 합 // n개)

# 이분탐색으로 t >= n 이되는 최대길이 찾기 
while l <= r:
    m = (l+r)//2

    # 각 랜선을 m으로 나눴을 때의 몫의 합 t 구하기
    t = 0
    for i in range(k):
        t += line[i] // m
        
    if t >= n :
        l = m+1
    else:
        r = m-1
    
# 최댓값이니까 r 
print(r)