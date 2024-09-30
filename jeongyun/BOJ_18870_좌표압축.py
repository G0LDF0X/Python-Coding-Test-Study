import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = []
ans = dict()
for i, x in enumerate(arr):
    arr2.append([i, x])
    ans[x] = -1
# print(ans)


arr2.sort(key= lambda x: x[1])
for i,x in enumerate(arr2):
    if ans[x] == -1:
        ans[x] = i
# print(ans)
for x in arr:
    print(ans[x], end=' ')