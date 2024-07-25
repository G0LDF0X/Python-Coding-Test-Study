import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())

computer_list = []

# append : 리스트 끝에 단일 요소를 추가. list를 append하면 다차원 배열이 됨.
# extend : 리스트 끝에 다른 리스트의 모든 요소를 추가. 즉, 리스트를 병합하는데 사용됨.
for i in range(N):
    computer_list.extend(list(map(int, input().split())))

computer_list.sort()

# 절반 이상이 냉방기의 차가운 공기를 받아야하므로, 중간값을 출력.

print(computer_list[len(computer_list) // 2])