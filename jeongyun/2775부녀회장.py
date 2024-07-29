import sys
input = sys.stdin.readline

t = int(input())

while t >0:
    t -=1
    
    k = int(input())
    n = int(input())
    
    # k 층의 n 호 에는 몇명이 거주 ? k-1층의 1호 ~ n호까지 거주민들의 합
    # 0층의 i 호에는 i 명 거주 
    # k 층까지 각 층의 n호에는 몇명 거주하는지 -> n-1 층의 1~n-1호를 알아야 함 
    
    apt = [[0] * (n + 1) for _ in range(k + 1)] 
    
    # 0층은 i로 초기화 
    for i in range(1, n + 1):
        apt[0][i] = i
        
    # print(apt)
    for i in range(1, k+1):
        for j in range(1, n+1):
            # 각 호수에 그 아래층의 같은 호수 + 현재 층의 앞 호수
            apt[i][j] = apt[i][j-1] + apt[i-1][j]
        # print(apt)
    print(apt[k][n])
    
# [1, 2, 3]
# [1, 3, 6]
# [1, 4, 10]
