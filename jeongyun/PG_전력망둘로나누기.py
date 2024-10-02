def solution(n, wires):
    answer = float('inf')
        
    for i in range(len(wires)):
        # 현재 wire 제외한 나머지 wire 들 가지고 그래프 만들기 
        new_wires = wires[:i] + wires[i+1:]
        graph = [[i] for i in range(n+1)]
        
        for wire in new_wires:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])
            
        # dfs 시 visited set 초기화
        visited = set()
        # 트리 dfs 탐색
        def dfs(v):
            visited.add(v)
            cnt = 1
            for node in graph[v]:
                if node not in visited:
                    visited.add(node)
                    cnt += dfs(node)
            return cnt
        
        # 현재 간선의 첫번째 노드에 연결된 노드 탐색
        w1 = dfs(wires[i][0])
        # 연결되지 않은 나머지 노드들 
        w2 = n - w1
        
        answer = min(answer, abs(w1 - w2))
    return answer
