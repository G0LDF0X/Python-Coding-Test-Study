import sys
input = sys.stdin.readline

n = int(input())

wait = []   # 기다리는 시간 담을 리스트 

for i in range(n):
    a, b = map(int, input().split())
    wait.append(a-b) 
    
wait.sort()

# n이 홀수면 중간값 1개만 답
if n %2 == 1: 
    ans = 1
# n이 짝수면 n//2 ~ n//2 -1 이하의 모든 수 
else:
    ans = abs(wait[n//2] - wait[n//2 - 1] + 1)

print(ans)