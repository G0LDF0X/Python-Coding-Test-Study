import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input().strip())

S = []

for _ in range(T):
    A, B = input().split()[0], input().split()[1]
    if A == "add" and B not in S:
        S.append(B)
    


        