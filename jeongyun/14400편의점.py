import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    arr.append([x,y])
    
# x 기준 오름차순 정렬 후 중간 값이 편의점의 x좌표
arr.sort(key = lambda x: x[0])
dx = arr[n//2][0]

# y 기준 오름차순 정렬 후 중간 값이 편의점의 y좌표
arr.sort(key= lambda x: x[1])
dy = arr[n//2][1]

# 총 거리의 합 계산
dist = 0
for i in range(n):
    dist += abs(dx - arr[i][0]) + abs(dy-arr[i][1])
    
print(dist)