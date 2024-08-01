import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 2 1 1 0 => 키가 i 인 사람 왼쪽에 나보다 키 큰 사람 몇명 있는지 
# (1, 2) (2, 1) (3, 1) (4, 0)       나보다 큰 사람 자리 앞에 두고 저장 _ _ 1 _ -> _ 2 1 _ -> _ 2 1 3 -> 4 2 1 3
# 4 2 1 3 
   
ans = [0 for _ in range(n)]

for i in range(n):
    cnt = arr[i]
    h = i+1
    for j in range(n):
        # ans 자리가 비어있으면 그 자리 저장
        if cnt == 0 and ans[j] == 0:
            ans[j] = h
            break
        # 자기 자리 아니면
        elif ans[j] == 0:
            cnt -=1
            
for i in range(n):
    print(ans[i], end=' ')