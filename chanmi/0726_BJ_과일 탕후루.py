import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())

fruit_list = list(map(int, input().split()))

# for문이 두 번 들어가서 시간 복잡도가 O(n^2)가 되었기 때문에 시간 초과가 발생한 것으로 보임.
# 따라서, 시간복잡도를 줄이기 위해 투 포인터를 사용

max_length = 0
start = 0

# 어떤 과일이 몇 개 들어있는지 카운트 하는 용도
fruit_count = defaultdict(int)

# for문을 통해 오른쪽 포인터를 0에서부터 출발해 계속 오른쪽으로 움직임.
# 오른쪽으로 계속 키워나가다가, 과일의 종류가 2개 이상이 되면 왼쪽 포인트를 오른쪽으로 옮김
# 왼쪽 포인트를 오른쪽으로 옮기면서, 해당 과일의 개수가 0이 되면 해당 과일을 삭제함
# 이 과정을 반복하면서, 가장 긴 길이를 찾아냄
for end in range(N):
    # 현재 오른쪽 포인터가 가리키고 있는 과일을 defaultdict에 추가
    fruit_count[fruit_list[end]] += 1

    # 현재 [start, end] 사이에 과일의 종류가 2개 이상이면
    while len(fruit_count) > 2:
        # start를 오른쪽으로 한 칸 움직이면서
        # defaultdict 안에 있는 해당 과일의 개수를 1개 줄임
        # [start, end] 사이의 과일이 2종류가 될 때까지 while문을 반복
        fruit_count[fruit_list[start]] -= 1
        if fruit_count[fruit_list[start]] == 0:
            del fruit_count[fruit_list[start]]
        start += 1

    # 이러면 while문이 끝났을 때, [start, end] 사이에는 과일이 두 종류만 남게 되므로
    # 기존의 max_length와 비교한다.
    max_length = max(max_length, end - start + 1)
print(max_length)