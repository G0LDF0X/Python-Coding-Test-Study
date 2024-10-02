import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

n,m = map(int, input().split())
graph = []
for i in range(n):
    x  = input().strip()
    graph.append(x)
    
ans = 1e19

# 전체에서 8*8만큼씩 떼어보면서 바꿔야될 알파벳 확인 
for i in range(n-7):
    for j in range(m-7):
        changeA, changeB = 0, 0
        # B로 시작하거나 / W로 시작하거나 둘 중 하나 , B로 시작: B는 i+j가 짝수 / W로 시작: W는 i+j가 짝수 
        for x in range(i, i+8):
            for y in range(j, j+8):
                if graph[x][y] == 'B':
                    if (x + y) %2 == 0:
                        changeB +=1
                    else:
                        changeA += 1
                else:
                    if (x + y) % 2 == 0:
                        changeA += 1
                    else:
                        changeB += 1
        ans = min(ans, changeA, changeB)
        
print(ans)