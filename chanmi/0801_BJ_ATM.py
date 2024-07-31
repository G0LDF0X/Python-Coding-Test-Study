import sys
import re
import copy

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
number_list = list(map(int, input().split()))
enumerate_list = list(enumerate(number_list))
enumerate_list.sort(key=lambda x: x[1])
answer_list = [x[1] for x in enumerate_list]
total_sum = answer_list[0]

for i in range(1, N):
    answer_list[i] += answer_list[i - 1]
    total_sum += answer_list[i]

print(total_sum)