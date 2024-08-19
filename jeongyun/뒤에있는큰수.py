# 스택 이용 풀이 
def solution(numbers):
    answer = [-1] * len(numbers)
    st = []
    
    for i in range(len(numbers)):
        while st and numbers[i] > numbers[st[-1]]:
            answer[st.pop()] = numbers[i]
            
        st.append(i)
    return answer



# # 시간 초과 풀이 => O(N^2)

# def solution(numbers):
#     answer = []
#     n = len(numbers)
#     cur = 0 
    
#     # 마지막 -1 까지만 반복함. -> 어차피 마지막은 -1임.
#     for i in range(n-1):
#         cur = numbers[i]
#         # 현재 i 번째 수보다 뒤에 있는 수 중 큰 수 나오면 answer에 저장. 바로 반복 종료
#         for j in range(i+1, n):
#             if numbers[j] > cur:
#                 answer.append(numbers[j])
#                 cur = numbers[j]
#                 break
#         # 현재 i 번째 수보다 큰 수가 없었을 경우. -1
#         if cur == numbers[i]:
#             answer.append(-1)
        
#     # 마지막 원소는 무조건 -1 
#     answer.append(-1)
#     return answer