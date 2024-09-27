import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input().strip())            #도시 가로크기
M = int(input().strip())            #도시 세로크기


road = []

for _ in range(M):
    road.append(list(input().strip()))


visited = [[0]*N for _ in range(M)]


