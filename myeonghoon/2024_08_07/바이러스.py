# 1  2  3  4
#  5  6  7

# 1 2 3 4 5 6 7
# index[1] = 2, 5
# index[2] = 3, 1
# index[3] = 2
# index[4] = 7 실행 x
# index[7] = 4 실행 x
# index[5] = 6
# index[6] = 5

# 1 -> 2(방문 완료) -> 3(방문 완료) -> 만약 3 다음이 null이면
# 다시 1 -> 5(방문 완료) -> 6(방문 완료) -> 다음이 null이면 
# 1에서 2와 5모두 방문을 완료하였으므로 2로 넘어가기
# 2와 연결된 모든 방향이 방문 완료하였으면
# 3으로 넘어가기 ... 배열 끝까지 반복

# 2랑 5를 방문하고 나서
# 2에 있는 3을 방문
# 3에서는 모두 방문 했으므로
# 1에 있는 5를 방문해야 한다.

# 먼저 1번 인덱스를 방문했다고 처리해야 하는데
# graph[1]의 값은 2,5이다. 1번은 방문 처리가 안되고, 2,5번은 방문을 안했다면 방문하고 방문처리를 해야하는데
# for i in graph[start]:         
#        visited[i] = True 이렇게 작성하면, 방문을 했는지 확인도 안하고 방문처리를 한 셈.
# 방문을 안했다면 방문을 하고 방문처리를 해야 한다.


def solution(computer, network, network_list):    
    graph = [[] for _ in range(computer + 1)]
    
    for x, y in network_list:
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (computer + 1)
    
    dfs(graph, 1, visited)

    return (visited.count(True)-1)


def dfs(graph, start, visited):
    # 2번 노드를 방문함
    visited[start] = True

    for i in graph[start]:         
        if visited[i] == False:
            dfs(graph, i, visited) # 2는 방문하지 않았으므로 2번 노드를 방문     
    


computer = int(input().strip())
network = int(input().strip())

network_list = []
for _ in range(network):
    n_list = list(map(int, input().split()))
    network_list.append(n_list)


print(solution(computer, network, network_list))