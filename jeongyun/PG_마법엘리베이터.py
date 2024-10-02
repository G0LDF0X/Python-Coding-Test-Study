def solution(storey):
    answer = 0
    # storey를 문자열로 변환 -> 일의 자리부터 확인하기 위해 뒤집기 
    s_storey = str(storey)
    s_storey = s_storey[::-1]
    
    c = 0   # 올림수 확인
    
    for i, s in enumerate(s_storey):
        # 올림 있으면 올림 처리 
        if c == 1:
            s = int(s) + 1
        # 현재 자리가 6~9 사이이면 올림 발생, 10이 되게 만들기
        if int(s) >= 6:
            c =1 
            answer += 10-int(s)
        # 현재 자리가 0~4 사이이면 올림x, 0이 되게 만들기 
        elif int(s) < 5 :
            c = 0
            answer += int(s)
        # 현재 자리가 5이면 다음 자리를 보고 올림 / 내림 결정
        elif int(s) == 5:
            # 다음 자리가 5 이상이면 올림
            if i+1 < len(s_storey) and int(s_storey[i+1]) >= 5:
                c = 1
                answer += 10 - int(s)
            # 다음 자리가 5 미만이면 내림
            else:
                c = 0
                answer += int(s)
    # 마지막에 올림수 발생해서 수의 자릿수가 바뀐 경우 추가된 자리 더하기: 56-> 60->100 -> 0 
    if c == 1:
        answer +=1
    return answer