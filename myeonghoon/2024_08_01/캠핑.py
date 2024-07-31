# 8일 중에 5일만 이용할 수 있고 휴가 20일짜리 8 / 8 / 4 -> 이번주에 5번, 다음 주에 5번, 그 다음 주에 4번 도합 14번
# 8일 중에 5일 휴가 17일 -> 8 / 8 / 1 -> 이번 주에 5번, 다음 주에 5번, 그 다음주에 1번 도합 11번

def solution(L, P, V):
    answer = 0
    answer = (int(V / P) * L) + (V % P)    
   
    return answer

L = 5 
P = 8
V = 17
print(solution(L, P, V))

L = 5 
P = 8
V = 20
print(solution(L, P, V))