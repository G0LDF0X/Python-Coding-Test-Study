def solution(book_time):
    answer = 1
    books = []
    
    # book_time을 분 단위 숫자로 변환 
    for book in book_time:
        s = int(book[0][:2]) * 60 + int(book[0][3:])
        e = int(book[1][:2]) * 60 + int(book[1][3:])
        books.append([s, e])

    # 대실 종료 시각 기준으로 오름차순 정렬
    books.sort(key = lambda x: (x[0], x[1]))
        
    # 대실 시작 시각이 이전 예약의 대실 종료시각 + 10분 보다 작으면 새로운 방 필요 
    # 대실 시작 시간 >= 이전 예약의 대실 종료시각 + 10분 : 그 방 그대로 대실
    # 이전 예약이라는 걸 방 마다 체크하고 있어야됨. 
    # 방이 하나 늘어나면 그 방의 이전 예약을 저장하는 리스트 필요. 
    # 그럼 대실 시작 시간을 모든 방의 이전예약과 비교하는 반복문 필요. 
    prev_books = [books[0][1]]
    for book in books[1:]:
        same = False

        for i in range(len(prev_books)):
            if book[0] >= prev_books[i]+10:
                prev_books[i] = book[1]
                same = True
                break

        if same == False:
            answer +=1
            prev_books.append(book[1])
        
    
    return answer