import sys
input = sys.stdin.readline

ans = 0

k, n = map(int, input().split())
line = []
for i in range(k):
    x = int(input())
    line.append(x)

# binary search 로 n개 이상을 만들 수 있는 최대 랜선 길이 찾기
    
line.sort()

l, r = 1, line[k-1]
while l<=r:
    m = (l + r) // 2
    lan = 0
    
    # m 길이로 자를 수 있는 랜선의 갯수 구하기 
    for x in line:
        lan += x // m
        
    if lan >= n:
        ans = max(m, ans)
        l = m+ 1
    else:
        r = m-1
print(ans)