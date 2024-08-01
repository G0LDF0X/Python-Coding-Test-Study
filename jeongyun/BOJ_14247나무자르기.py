import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))
grow = list(map(int, input().split()))

tree  = []
for i in range(n):
    tree.append([height[i], grow[i]])
    
tree.sort(key=lambda x: -x[1])

ans = 0
for i in range(n):
    # 하루에 한 나무씩 선택 => 그 날 가장 길이가 긴 나무 선택 xxxxx / 다음날 자란 길이가 더 긴 나무가 현재 가장 긴 나무보다 더 클 수 있음. 
    # 성장 길이가 가장 작은 것부터 자르기 -> 가장 많이 자라는 나무는 최대한 늦게 잘라서 최대 길이 얻게 
    # 다음날 나무 길이 = 전 날의 나무 길이 + grow 

    ans += tree[i][0] + (tree[i][1] * (n-i-1))  
    
    # print(tree[i], n-i)
print(ans)

# 6 10 12 14 14 

31 + 16 + 8 + 3 + 6