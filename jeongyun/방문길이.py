def solution(dirs):
    answer = 0
    visited = set()
    
    # 시작은 5, 5에서 시작 
    x, y = 5, 5
    i = -1
    for dir in dirs:
        i += 1
        nx, ny = x, y
        
        # 방향 체크 && 경계 체크 
        if dir == 'U':
            if y < 10:
                ny += 1
        elif dir == 'D':
            if y > 0:
                ny -= 1
        elif dir == 'R':
            if x < 10:
                nx += 1
        elif dir == 'L':
            if x > 0:
                nx -= 1
        # x,y 에서 nx,ny 로 가는것, nx, ny에서x,y로 가는 경로 둘 다 체크 
        if (x, y) != (nx, ny):
            if (x, y, nx, ny) not in visited and (nx, ny, x, y) not in visited:
                visited.add((x, y, nx, ny))
                visited.add((nx, ny, x, y))
                answer +=1
            x, y = nx, ny
        
    return answer