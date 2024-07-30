#백준 1184번 약속
import sys

# 입력 받기
n = int(sys.stdin.readline().strip())
appointments = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Ai - Bi의 차이를 저장할 리스트
diffs = []

# 모든 Ai, Bi 쌍에 대해 Ai - Bi의 차이를 계산
for a, b in appointments:
    diffs.append(a - b)

# diffs 리스트를 정렬
diffs.sort()

# 중간값 찾기
if n % 2 == 1:
    median_diffs = [diffs[n // 2]]
else:
    median_diffs = [diffs[n // 2 - 1], diffs[n // 2]]

# 최소 기다리는 시간의 합 계산
min_waiting_time = float('inf')
for median in median_diffs:
    waiting_time = sum(abs(diff - median) for diff in diffs)
    min_waiting_time = min(min_waiting_time, waiting_time)

# 가능한 T 값의 개수 찾기
# diffs의 중복된 값들 사이에 있는 모든 정수 값들이 가능한 T 값이 될 수 있음
unique_diffs = sorted(set(diffs))
gap_count = 0
for i in range(len(unique_diffs) - 1):
    # 인접한 두 값 사이의 정수 개수를 세어 gap_count에 더함
    gap_count += unique_diffs[i + 1] - unique_diffs[i] - 1

# 가능한 T 값의 개수는 유니크한 diffs의 개수 + 사이의 간격(gap_count)
print(len(unique_diffs) + gap_count)