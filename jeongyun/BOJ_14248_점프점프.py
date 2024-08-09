import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

visited = [-1] * (n+1)
ans = []

def dfs(x):
    if x < 1 or x > n or visited[x] == 1:
        return
    visited[x] = 1
    ans.append(x-1)
    dfs(x + arr[x-1])
    dfs(x - arr[x-1])
    
dfs(s)
set(ans)

print(len(ans))