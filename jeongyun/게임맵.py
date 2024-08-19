from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)   # 전체 세로 길이 
    m = len(maps[0])    # 한 줄의 가로 길이 
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # bfs 로 0,0 에서 n, m까지의 최단경로 구함. 
    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # if visited[nx][ny]
            if maps[nx][ny] ==1:
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
                
    # 목적지 (n, m)의 값이 1이면 : 해당 칸까지의 가능한 경로가 없었다는 것을 의미 -> -1 출력  / 1이 아니면 해당 거리 출력
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]
            
    return answer


