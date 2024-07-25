import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())

fruit_list = list(map(int, input().split()))

# 완전 탐색으로 접근하기

# 앞에서 빼는 a가 0개일 경우
# 0번째 인덱스부터 세어서 과일이 2개가 되는 리스트의 길이를 반환

# 앞에서 빼는 a가 1개인 경우
# 1번째 인덱스부터 세어서 과일이 2개가 되는 리스트의 길이를 반환

# 이 경우 리스트의 전체를 모두 봐야 하므로 20만번을 카운트함

# 반대로 뒤에서 빼는 b가 0개인 경우
# -1번째 인덱스부터 세어서 과일이 2개가 되는 리스트의 길이를 반환

# 뒤에서 빼는 b가 1개인 경우
# -2번째 인덱스부터 세어서 과일이 2개가 되는 리스트의 길이를 반환

# 이렇게 해서, 그때그때 max_length의 길이를 파악해 반환하면 됨

max_length = 0
for i in range(N):
    a = 0
    b = 0
    fruit_kind = set()

    for j in range(i, N):
        fruit_kind.add(fruit_list[j])

        if len(fruit_kind) <= 2:
            max_length = max(max_length, j - i + 1)
        elif len(fruit_kind) > 2:
            break

print(max_length)