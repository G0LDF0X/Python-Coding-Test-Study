import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

while True:
    command = input().rstrip()
    if command == '0':
        break
