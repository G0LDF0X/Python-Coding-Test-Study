def solution(m, n, board):
    block_list = []
    count = 0
    
    for block in board:
        block_list.append(list(block))
    
    while True:
        match_list = [[0] * n for _ in range(m)]
        
        for i in range(m - 1):
            for j in range(n - 1):
                # 가로로 두칸 확인
                if block_list[i][j] == block_list[i][j + 1]:
                    # 세로로 두 칸 확인
                    if block_list[i][j] == block_list[i + 1][j]:
                        # 대각 확인
                        if block_list[i][j] == block_list[i + 1][j + 1]:
                            match_list[i][j] = 1
                            match_list[i + 1][j] = 1
                            match_list[i][j + 1] = 1
                            match_list[i + 1][j + 1] = 1
        # 하나 이상 터진 경우
        if any(1 in row for row in match_list):
            for i in range(m):
                for j in range(n):
                    if match_list[i][j] == 1:
                        block_list[i][j] = "-"
            
            for j in range(n):
                empty_slots = []
                for i in range(m - 1, -1, -1):
                    if block_list[i][j] == "-":
                        empty_slots.append(i)
                    elif empty_slots:
                        empty_index = empty_slots.pop(0)
                        block_list[empty_index][j] = block_list[i][j]
                        block_list[i][j] = "-"
                        empty_slots.append(i)
            
            count += sum(sum(row) for row in match_list)
        else:
            break

    return count