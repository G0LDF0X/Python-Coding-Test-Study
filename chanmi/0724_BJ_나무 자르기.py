import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 필요한 나무 길이 M
# 나무의 수 N
# 길이 M의 나무를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값 H

# 1 ≤ N ≤ 1,000,000
# 1 ≤ M ≤ 2,000,000,000
# 0 ≤ H ≤ 1,000,000,000

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort()

# 나무의 start가 0인 이유 : 모든 나무를 잘라야 M을 만족하는 경우도 생기기 때문

start = 0
end = max(tree_list)

while start <= end:
    mid_value = (start + end) // 2

    tree_sum = 0
    for tree in tree_list:
        if tree > mid_value:
            tree_sum += tree - mid_value

    # 나무를 충분히 자른 경우에는, 나무를 자르는 높이를 올리면 됨.
    # 즉, start를 증가시키면 됨.
    if tree_sum >= M:
        start = mid_value + 1

    # 나무가 모자란 경우에는, 나무를 더 낮은 높이에서 잘라야 함.
    # 즉, end를 감소시켜야 함.
    else:
        end = mid_value - 1

# while문이 끝나는, start가 end를 추월하는 것은 내가 현재 얻은 나무가 M보다 많거나 같을 때다.
# 즉, 직전의 start와 end 값이 동일하며, 이때 여전히 tree_sum이 M보다 크거나 같다는 말이므로,
# start는 mid_index + 1이 되었으므로 아직 변하지 않은 end를 출력하면 된다.
print(end)