import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
number_list = list(map(int, input().split()))
K = int(input().strip())

# 문제에 대한 이해 및 완전 탐색

# 예제 입력 1
# N = 5
# number_list = [1, 2, 3, 2, 1]
# K = 7

# [1, 2, 3, 2, 1]을 슬라이싱 해서 합했을 때 7 초과가 나오는 리스트의 개수를 구하는 문제
# 1. [1, 2, 3, 2] : 합계 8 (0번 인덱스부터 3번 인덱스까지)
# 2. [1, 2, 3, 2, 1] : 합계 9 (0번 인덱스부터 4번 인덱스까지)
# 3. [2, 3, 2, 1] : 합계 8 (1번 인덱스부터 4번 인덱스까지)
# 이라서 3이 정답이다.

# 즉, 완전 탐색으로 접근한다면
# [0:1], [0:2], [0:3], ... [0:N], [1:2], [1:3], ... [1:N], ... [N-1:N]까지 모두 탐색해야 한다.
# 1 <= N <= 100000이므로 완전탐색을 하면 시간복잡도는 O(N^2)이 되므로,
# 총 10^10번의 연산을 수행해야 한다.

# 이를 투 포인터로 접근한다면
# 1. start와 end를 0으로 초기화한다.
# 2. start와 end 사이의 합이 K보다 작으면 end를 증가시킨다.
# 3. start와 end 사이의 합이 K보다 크거나 같으면, end의 뒤쪽에 있는 원소를 다 더해도 K보다 크므로, 
#     list_count에 남은 원소의 개수를 더하고, start를 증가시킨다.
# 4. start가 N보다 작을 때까지 반복한다.

# 이런 방식으로 풀이가 가능할 것으로 보인다.

start = 0
list_count = 0

for end in range(N):
    if start == N:
        break

    # 구간 내의 합이 K보다 크면, end 뒤쪽에 있는 원소는 더해도 K보다 크므로,
    # list_count에 남은 원소의 개수를 더하고, start를 증가시킨다.
    if sum(number_list[start:end + 1]) > K:
        list_count += N - end
        start += 1
        while sum(number_list[start:end + 1]) > K:
            list_count += N - end
            start += 1
        continue

    # 구간 내의 합이 K보다 작으면, end를 증가시킨다.
    else:
        continue
        
print(list_count)