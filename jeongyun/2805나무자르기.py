import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
s = 1
e = max(tree)

while s <= e:
    mid = (s + e) // 2
    
    cut = 0 
    for t in tree:
        if t >= mid:
            cut += (t - mid)
    if cut >= m:
        s = mid+1
    else:
        e = mid-1
        
print(e)

