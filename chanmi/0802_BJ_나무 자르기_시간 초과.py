import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 산에는 N개의 나무가 있으며,
# 영선이는 하루에 한 나무씩, N일동안 산에 오르며 나무를 자른다.

# 첫째줄 : 첫날 올라갔을 때 길이
# 둘째줄 : 나무들이 자라는 속도

# 예제 입력 1
# 5
# 1 3 2 4 6
# 2 7 3 4 1

# 맨 처음에는 그때그때 가장 큰 나무를 자르려고 했지만, 그때는 얻을 수 있는 나무의 길이가 56이었음.
# 적게 자라는 것부터 자르면...?

# 1일차에 4번째 인덱스의 나무를 자른다. 총 자른 나무의 길이는 6(+6)이 되고,
# 1 3 2 4 0이 되고, 밤에는 3 10 5 8 1이 된다.

# 2일차에 0번째 인덱스의 나무를 자른다. 총 자른 나무의 길이는 9(+3)가 되고,
# 0 10 5 8 1이 되고, 밤에는 2 17 8 12 2가 된다.

# 3일차에 2번째 인덱스의 나무를 자른다. 총 자른 나무의 길이는 17(+8)가 되고,
# 2 17 0 12 2가 되고, 밤에는 4 24 3 16 3이 된다.

# 4일차에 3번째 인덱스의 나무를 자른다. 총 자른 나무의 길이는 33(+16)이 되고,
# 4 24 3 0 3이 되고, 밤에는 6 31 6 4 4가 된다.

# 5일차에 1번째 인덱스의 나무를 자른다. 총 자른 나무의 길이는 64(+31)이 되고,
# 6 0 6 4 4가 된다.

# 따라서 enumerate로 정렬한 뒤, 적게 자라는 나무부터 자르면 된다.

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

# for문을 두 번 쓰면 10만의 제곱이라 시간초과가 발생할 것 같은데.....
for i in range(N):
    answer += total_list[i][1]
    total_list[i][1] = 0

    for j in range(N):
        total_list[j][1] += total_list[j][2]

print(answer)