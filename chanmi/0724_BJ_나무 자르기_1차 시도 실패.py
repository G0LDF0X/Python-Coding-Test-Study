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
tree_len = N

# 10 15 17 20
# 15를 기준으로 자른다면, 15보다 뒤쪽에 있는 뒷값에 전부 15를 빼고 남은 값의 합이 가져갈 수 있는 나무가 됨
# 17을 기준으로 자른다면, 17보다 뒤쪽에 있는 뒷값에 전부 17을 빼고 남은 값의 합이 가져갈 수 있는 나무가 됨

while True : 
    middle_value = tree_list[tree_len // 2 - 1]
    print(middle_value, tree_list)
    sum_value = 0

    for item in tree_list[tree_len // 2 - 1: ]:
        sum_value += item - middle_value
    
    # 아직 M만큼 가져가지 못함
    if sum_value < M:
        tree_list = tree_list[tree_len // 2 - 1:]
        tree_len = len(tree_list)

        # 하나만 남은 경우
        if tree_len == 1:
            print(tree_list[0])
            break
    else:
        print(middle_value)
        break
