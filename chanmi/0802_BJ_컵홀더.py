import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 인접한 좌석 사이에는 컵홀더가 하나씩 있고, 맨 끝에는 양쪽에 하나씩 더 있다.
# 커플석 사이에는 컵홀더가 없다.

# S는 일반석, L은 커플석. L은 무조건 두 개씩 붙어있다.
# 따라서 SLLLLSSLL일때 컵홀더를 *로 표기하면
# *S*LL*LL*S*S*LL*이 된다.

# 이 경우, 컵홀더를 쓰지 못하는 사람을 ()로 표기하면
# *S *L L* (L) L* S* S* (L) L*이 되므로
# 총 두 명은 컵홀더를 쓰지 못하게 된다.

# return 값으로는 컵홀더를 쓸 수 있는 사람의 수를 출력하면 된다.

# LL 좌석이 들어오면, 쓸 수 있는 컵의 개수가 1개 줄어든다.
# LL 좌석이 1개인 경우에는, 그래도 모든 사람이 쓸 수 있지만,
# LL 좌석이 2개 이상인 경우에는, 컵홀더를 쓸 수 없는 사람이 1명씩 늘어난다.
# 따라서 컵을 쓸 수 있는 사람은 N명 - LL 좌석의 개수 + 1이 된다.

# 1 ≤ N ≤ 50
N = int(input().strip())
seats = input().strip()

LL_count = seats.count('LL')

# min을 해주는 이유는, SSS 같은 경우에는 LL_count가 0이 되어버리기 때문에 결과값이 N + 1이 되는 것을 막기 위해서다.
print(min(N, N - LL_count + 1))