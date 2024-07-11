answer = 0
def solution(k, dungeons):
    global answer
    visited = [0 for _ in range(len(dungeons))] 
    # print(visited)
    
    def dfs(k, dungeons, visited, cnt):
        global answer
        if cnt > answer:
            answer = cnt
        # print(answer, cnt)
        
        for i in range(len(dungeons)):
            if visited[i] == 0 and k >= dungeons[i][0]:
                visited[i] = 1
                dfs(k - dungeons[i][1], dungeons, visited, cnt+1)
                visited[i] = 0
                
    dfs(k, dungeons, visited, 0)
    return answer