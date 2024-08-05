import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
P = list(map(int, data[1:]))

P.sort()
total_sum = 0

for i in range(N):
    total_sum += (i+1)*P[N-(i+1)]

print(total_sum)


#for i in range(N):
    # total_sum += (i+1)*P[N-i]
#이렇게 하니 계속 런타임 에러가 났었다.