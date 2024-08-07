# 깊이 우선 탐색? 이라는 걸 해야될 것 같은데?
# '-' 와 '|' 이 두개 밖에 없다.
# -, --, ---, ---- 전부다 1개로 취급
# -|, |-, 각각 1개 1개
# | - | 
# | | -
# -일때 자신의 오른쪽에 -가 아니라 |
# 행은 |을 중심으로 나눠야한다. 
# 열은 -을 중심으로 나누는 게 좋을 것 같다.

# 인접한 나무 판자를 찾는 과정....
# 0,0 이 - 이라면 인접한 나무 판자를 찾기 위해선 오른쪽으로 이동해야 함
# 0, 1 - 이라면 -> 오른쪽이로 이동
# 0, 2 가 | 라면 -> 밑으로 이동(|의 인접한 나무 판자를 찾기 위해서는 열로 이동해야 되기 때문)
# 1, 2 가 | 라면 -> 밑으로 한 칸 더 이동
# 1, 3 이 - 라면 -> 판자의 갯수를 1개 증가지키고 오른쪽으로 이동
# 만약 오른쪽에서 벽을 만났다면
# 0,1 로 이동 -> 이미 방문 했다면
# 0,3 으로 이동 -> 0,3 은 방문하지 않았으므로 dfs 탐색
# 

def solution():
    pass

