import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
P = list(map(int, data[1:]))

P.sort()
total_sum = 0

for i in range(N):
    total_sum += (i+1)*P[N-i]

print(total_sum)
