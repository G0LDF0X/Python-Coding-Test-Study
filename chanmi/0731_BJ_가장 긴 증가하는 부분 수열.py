import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1 <= N <= 1000
N = int(input().strip())

# 10 20 10 30 20 50
# 각 배열의 길이 중 가장 큰 값을 저장하는 리스트를 만들어본다면....

# 맨 처음에는 전부
# 1 1 1 1 1 1

# 그리고 인덱스의 값을 하나씩 보면서, 앞쪽의 값과 비교하기
# 큰 경우에만 max값 저장하기
# i = 1 (20일 때)
# 1 2 1 1 1 1

# i = 2 (10일 때)
# 1 2 1 1 1 1

# i = 3 (30일 때)
# 30은 10 20 30으로 길이가 3이 될 수도 있고,
# 20 30으로 길이가 2이 될 수도 있고,
# 10 30으로 길이가 2가 될 수도 있다.
# 이중에서 가장 긴 건 3이므로
# 1 2 1 3 1 1로 업데이트한다.
# 이는 기존 값에서 가장 큰 값인 2에 +1을 한 값과 같다.

# i = 4 (20일 때)
# 20은 10 20으로 길이가 2인게 최대다.
# 1 2 1 3 2 1

# i = 5 (50일 때)
# 50은 10 20 30 50으로 길이가 4인게 최대다.
# 1 2 1 3 2 4이므로, 이것도 최대값인 3에 +1을 한 값이다.

# 이런식으로 쪼개서 DP(Dynamic Programming)으로 접근해보면 될 것 같다.

number_list = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        # 현재 값(number_list[i])이 이전 값(number_list[j])보다 큰 경우에만
        # dp[i]에 dp[j] + 1을 저장한다.
        # 그리고 max와 비교하여 더 큰 값으로 교체해준다.
        if number_list[i] > number_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))