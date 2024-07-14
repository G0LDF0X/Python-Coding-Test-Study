# 각 숫자 앞자리부터 비료해야 한다.
# 예를 들어 먼저 입력한 전화번호가 133 이라면
# 그 뒤 전화번호가 133 157일 경우 133을 입력하면 먼저 입력한 전화번호가 울리기 때문
# 133 157은 'No' 가 떠야하고
# 133 은 'Yes'가 떠야함
# 먼저 133 을 입력했다고 치면
# 1, 3, 3출력
# 인덱스 0번부터 비교해서 
# 연속된 숫자가 같은지 어떻게 알까?
# 앞에서부터 비교해서 133까지가 한 번도 어긋나면 안됨
# 만약 113이런 식으로 중간에 한 번 어긋나면 일관성이 전혀 없는 전화번호
# 두 전화번호의 길이를 구해서 정렬해야 되나?
# 만약 앞쪽에 긴 전화번호가 있고 뒤 쪽에 짧은 전화번호가 있다면 긴 전화번호에 대한 일관성 검증은 의미 없음.
# 숫자 배열 중간에 
# 

p_num_1 = '133'
p_num_2= '133157'
consistency = []

if len(p_num_1) < len(p_num_2): # 비교하는 전화번호의 길이가 더 작아야 성립.
    for i in range(len(p_num_1)):
        if p_num_1[i] == p_num_2[i]:
            consistency.append('True')
        elif p_num_1[i] != p_num_2[i]:
            consistency.append('No')

# for문이 끝날 때까지 consistency에 담긴 원소들이 전부 True라면





# try:
#     for i in range(len(p_num_1)):
#         if p_num_1[i] == p_num_2[i]:
#             continue
#         elif p_num_1[i] != p_num_2[i]:
#             print('No')
#             break
#         print('Yes')
# except IndexError:
#     print('Yes')

    


# if p_num_1 in p_num_2:
#     print('No')
# else:
#     print('Yes')
