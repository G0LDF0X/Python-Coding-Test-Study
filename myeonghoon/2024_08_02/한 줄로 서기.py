# 아침에 밥을 먹기 위해서 줄 서는 사람의 수 : N
# 밥 먹을 때 내 앞에 있는 키 큰 사람의 수를 기억함.
# 1 부터 N까지 키가 순차적으로 올라감.
# 4 2 1 3이렇게 줄을 서 있을 때 
# 1보다 순서로는 앞에 있으면서 1보다 큰 수는 2
# 2보다 큰 수는 1
# 3보다 큰 수는 1
# 4보다 큰 수는 0
# 2 1 1 0 -> 1보다 큰 수는 2, 3, 4
# 2보다 큰 수는 3,4 / 2보다 큰 키는 1명/ 조합은 (4, 3, 2), (3, 4, 2), (4, 2, 3), (3, 2, 4)...(2,x, x)
# 규칙을 적용하면 4는 3보다 앞에 먼저 줄을 섰다 -> (4, 3, 2), (4, 2, 3), (2,x, x)
# 그리고 2보다 큰 키는 1명 밖에 없다. -> (4, 2, 3)
# 
# 3보다 큰 수는 4, 3보다 큰 키는 1명 == 3보다 큰 키는 4밖에 없음 -> 일단 4는 3보다 앞에 줄 섬.
# 4보다 큰 수는 없음.

# 1, 2, 3, 4가 있음
# 4보다 큰 숫자는 없음. 위치 이동 x
# 4는 3보다 앞에 있어야 됨으로 4랑 3위치를 교환한다 1, 2, 4, 3
# 2보다 큰 수는 3, 4 -> 2보다 큰 키가 1명 앞으로 와야되는데 우선순위가 높은 4랑 교환, 1, 4, 2, 3
# 1보다 큰 수는 2, 3, 4 -> 1보다 큰 키가 2명 앞으로 와야되는됨/ 1,4 교환(4, 1, 2, 3) / 1, 2 교환 (4, 2, 1, 3)


N = int(input().strip())
switch_num = list(map(int, input().split()))

def solution(N, switch_num):
    answer = []
    temp = 0
    
    for i in range(1, N+1):
        answer.append(i)

    for i in range(N-1, -1, -1):
        # answer[i] # answer[3] = 4
        for j in range(switch_num[i]): # switch_num[3] = 0, switch_num[2]=1 switch가 2면 0, 1 i+0, i+1, i+2
            index = i+j
            temp = answer[index] # 3
            answer[index] = answer[index+1] # 1, 2, 4, 4
            answer[index+1] = temp # 1, 2, 4, 3
    
    return answer

print(solution(N, switch_num))