# "mumu", "soe", "poe", "kai", "mine"
# "mumu", "soe", "kai", "poe", "mine"
# "mumu", "kai", "soe", "poe", "mine"
# "mumu", "kai", "soe", "mine", "poe" 
# "mumu", "kai", "mine", "soe", "poe" 


# 1. players 리스트의 각 요소와 그 인덱스를 딕셔너리에 저장합니다.
# 2. callings 리스트를 순회하면서 각 호출된 선수의 인덱스를 딕셔너리에서 찾습니다.
# 해당 선수의 인덱스가 0보다 큰 경우, 즉 첫 번째 요소가 아닌 경우에만 그 선수와 앞의 선수의 위치를 바꿉니다.
# 위치를 바꾼 후, 딕셔너리 player_indices를 업데이트하여 변경된 인덱스를 반영합니다.
def solution(players, callings):
    answer = []
    player_indices = {player: idx for idx, player in enumerate(players)}
    
    for i in range(len(callings)):
        player_idx = player_indices[callings[i]]
        players[player_idx], players[player_idx - 1] = players[player_idx - 1], players[player_idx]
        
        player_indices[players[player_idx]] = player_idx
        player_indices[players[player_idx - 1]] = player_idx - 1
    
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))

