import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1 ≤ N ≤ 100,000
N = int(input().strip())
tree_height = list(map(int, input().split()))
grow_speed = list(map(int, input().split()))

total_list = []
for i in range(N):
    total_list.append([i, tree_height[i], grow_speed[i]])

# 자라는 속도를 기준으로 오름차순 정렬
total_list.sort(key=lambda x: x[2])

answer = 0

# 이중 for문으로 인해 시간 복잡도가 O(n^2)이 되어 시간초과가 발생한 것으로 추정.

# 결국 나무의 길이란, 첫날의 길이에 지난 날짜만큼 자라는 속도를 더한 값이다.
# 같은 나무를 두 번 베지 않기 때문에 연산이 가능하다.
for i in range(N):
    answer += total_list[i][1] + total_list[i][2] * i

print(answer)