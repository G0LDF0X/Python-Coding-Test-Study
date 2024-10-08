import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

ans = 0     # 현재 최댓값
max_sum = -float('inf') # 최종 최대 합 : 가장 작은 수로 정의

for i in range(n):
    # 지금까지의 합과 현재 원소 중 큰 값으로 최댓값 업데이트
    ans = max(arr[i], ans+arr[i])
    # 최종 최대 합 업데이트 
    max_sum = max(max_sum, ans)
    print(max_sum, ans)
print(max_sum)

# 10 -4 3 1 5 6 -35 12 21 -1

#2 1 -4 3 4 -4 6 5 -5 1

