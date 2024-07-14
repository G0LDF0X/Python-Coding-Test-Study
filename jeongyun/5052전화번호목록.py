t = int(input())
for i in range(t):
    phone = []  # 전화번호 목록 배열
    con = True  # 일관성 여부 체크 
    n = int(input())    # 전화번호 갯수 
    
    # 전화번호 입력받아서 phone 에 저장
    for j in range(n):
        phone.append(input())
        
    # 전화번호 목록 정렬 : 오름차순으로 정렬 + 길이 순으로 정렬 
    phone.sort(key = lambda x: (x, len(x)))
    
    # 전화번호 목록에서 일관성 여부 체크 
    for j in range(n-1):
        # 현재 번호가 다음 번호의 접두어가 되면 일관성 없음 -> no
        if phone[j] == phone[j+1][:len(phone[j])]:
            con = False
            print('NO')
            break
    # 전체 전화번호목록에서 접두어 없이 일관성 있으면 yes 
    if con == True:
        print('YES')
    