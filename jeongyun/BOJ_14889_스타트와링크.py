import sys
from itertools import combinations
input = sys.stdin.readline

ans = float('1e19')
n = int(input())
s = []
for i in range(n):
    x = list(map(int, input().split()))
    s.append(x)
    
p = [i for i in range(n)]   # 0번부터 n-1번까지의 사람 

# n개 중 n/2개를 뽑는 조합 
comb = list(combinations(p, n//2))

# 각 팀에서 2명씩 조합했을 때 가능한 모든 조합의 능력치의 합 구하기
for c in comb:
    teamA = list(combinations(c, 2))
    scoreA = 0
    # print(c, set(p)-set(c))
    for x in teamA:
        i, j = x[0], x[1]
        scoreA += s[i][j] + s[j][i]
    # print(team)
    b = list(set(p)-set(c))
    teamB = list(combinations(b, 2))
    scoreB = 0
    # print(teamB)
    for x in teamB:
        i, j=x[0],x[1]
        scoreB += s[i][j] + s[j][i]
    ans = min(ans, abs(scoreA-scoreB))
print(ans)