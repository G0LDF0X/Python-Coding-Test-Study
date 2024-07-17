# 9시 43분

# 다리는 1개고 bridge_length는 다리의 길이이다.
# 만약 bridge_length가 100이면 100대의 트럭이 서 있을 수 있고
# bridge_length가 100인데 트럭이 1대이면 101초의 시간을 들여서 
# 다리를 지나갈 수 있다.(다리를 지나가는 시간 100초, + 나가는 시간 +1초) 
# weight는 다리가 지탱할 수 있는 무게의 한계치이다. 
# weight가 10이라면 트럭의 무게 총합이 10이하일 때만 다리에 올라갈 수 있음
# 만약 무게의 합이 10 인데 7인 트럭이 올라왔다면 다리를 다 건널 때까지 기다려야 함.

def solution(bridge_length, weight, truck_weights):
    answer = 0  
    return answer


def test_1(bridge_length, weight, truck_weights):
    answer = 0 # 지나가는데 걸린 시간 
    truck_passing_by_bridge = [] # 건너가는 중
    truck_passed_by_bridge = [] # 건넜음.
    # truck_weights = 대기중
    
    while(truck_weights):
        if truck_passing_by_bridge:
    
            if truck_weights[0] + sum(truck_passing_by_bridge) <= weight:
                truck_passing_by_bridge.append(truck_weights[0]) # 다리 건너는 중
                del truck_weights[0] # 맨 앞줄 트럭 삭제
                            
                answer += 1 # 먼저 달리고 있는 트럭이 있다면 +1 초                

                if count == bridge_length:
                    truck_passed_by_bridge.append(truck_passing_by_bridge[0]) # 다리를 다 건넜다면 
                    del truck_passing_by_bridge[0] 
                    # 이거 바로 삭제하면 안됨...
                    count = 0

        else:
            truck_passing_by_bridge.append(truck_weights[0]) # 다리 건너는 중
            del truck_weights[0] # 맨 앞줄 트럭 삭제

            for _ in range(bridge_length): # 먼저 달리고 있는 트럭이 없다면 bridge_length초 
                answer += 1

            truck_passed_by_bridge.append(truck_passing_by_bridge[0]) # 다리를 다 건넜다면 
            del truck_passing_by_bridge[0] 

    # for문 나갈 때 +1 초
    answer += 1
    return answer


def test_2(bridge_length, weight, truck_weights):
    answer = 0 # 지나가는데 걸린 시간
    bridge = [] # bridge_length미만
    bridge_weigth = 0 # 한계치
    
    answer += 1 # 트럭이 다리를 지나감
    # truck_weights에 있는 걸 빼서 bridge에 담자
    move = truck_weights.pop(0)
    bridge.append(move)

    while bridge:
        if bridge_weigth <= weight:
            # 무게가 무게치보다 낮다면
            
        
    
    

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# 답은 8초
print(solution(bridge_length, weight, truck_weights))


bridge_length = 100
weight = 100
truck_weights = [10]
# 답은 8초
print(solution(bridge_length, weight, truck_weights))


bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
# 답은 8초
print(solution(bridge_length, weight, truck_weights))


# 일단 바구니 같은 곳에다가 담아야 할듯
# 시간 | 건넘 | 건너가는 중 | 대기중
#   1               4         5,6,7 만약 건너가려는 트럭과 건너가는 중인 트럭의 합이 한계 무게치보다 작다면 트럭은 건널 수 있다.
#   2               [4,5]      6,7
#   3     4         [5,]           5와 6은 11이므로 10을 넘는다
#   4     [4,5]      6          7
#   5       4,5,6    7          x  이러면 5초인데 트럭 순서를 바꿀 수 없나봄.

#   0                         [7,4,5,6] 여기서 건너가는 중을 탐색한다.
#   1                7         [4,5,6]  시간을 어떻게 나타내지?
#   2                7         [4,5,6]  혼자 건너갈 때는 2초 다 먹는데 같이 건너갈 때는 (만약 다리를 건너가는 시간이 100초이고, 3대가 지나간다면 처음 차는 100초, 앞에 달리는 차가 있다면 +1초씩 더해준다)
#   3     7          4         [5, 6] 완전히 건너기 전까지는 건너가는 중인 상태가 되어야 한다.
#   4     7         [4, 5]       6 

# 굳이 for문을 돌려서 +2 를 해줄 필요있나?
# 트럭이 다리를 지나갈 때 +1
# 트럭이 다리를 지나가고 있는데 뒤에 트럭이 진입 못할 경우 배열의 길