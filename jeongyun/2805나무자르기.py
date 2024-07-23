import sys

def binary_search(tree, start, high):
    global result
    mid = (start + high) // 2
    cut_tree = 0
    
    if start > high:
        return result
    
    for t in tree:
        if t - mid < 0:
            break
        else:
            cut_tree += t - mid
    
    if cut_tree >= m:
        result = max(result, mid)
    
    if cut_tree > m:
        return binary_search(tree, mid + 1, high)
    else:
        return binary_search(tree, start, mid - 1)


n, m = map(int, sys.stdin.readline().split())
tree = [int(sys.stdin.readline()) for _ in range(n)]

tree.sort(reverse=True)
MAX = tree[0]

print(binary_search(tree, 0, MAX))

