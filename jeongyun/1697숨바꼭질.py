# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
# 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

from collections import deque
import sys 
input = sys.stdin.readline

n, k = map(int, input().split())

# n -> k로 변환 
# 1. n +1 , 2. n-1, 3. 2*n 의 경우로 이동 가능 -> n에서 k로 가는 bfs 

q = deque()
q.append((n, 0))

ans = 0
visited = [False] * 100001
visited[n] = True

while q:
    x, y = q.popleft()  # x: 현재 수, y : 거리 
    
    if x == k:  # k에 도착했으면 그때 거리 반환
        ans = y
        break
    
    if x+1 <=100000 and visited[x+1] == False:
        visited[x+1] = True
        q.append((x+1, y+1))    # x+1 로 갈 수 있으면 x+1과 y+1(거리 + 1)
    if x-1 >=0 and visited[x-1] == False:
        visited[x-1] = True
        q.append((x-1, y+1))    # x-1 로 갈 수 있으면 x-1과 y+1(거리 + 1)
    if x*2 <= 100000 and visited[x*2] == False:
        visited[x*2] = True
        q.append((x*2, y+1))    # x*2 로 갈 수 있으면 x*2과 y+1(거리 + 1)
        
print(ans)