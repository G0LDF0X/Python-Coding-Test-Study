def solution(record):
    # record의 가장 앞에 오는 건 Enter, Leave, Change 세 가지
    # uid로 사람을 구분
    user_dict = {}
    for i in range(len(record)):
        record_list = record[i].split()
        
        # 새로 입장한 경우 닉네임을 등록해줌(보통 새로 Enter한 경우)
        if record_list[1] not in user_dict:
            user_dict[record_list[1]] = record_list[2]
        else:
            # 이미 Enter 한 이후 Leave, Leave 한 뒤 새로 Enter, Change하는 경우
            if record_list[0] == "Change" or record_list[0] == "Enter":
                user_dict[record_list[1]] = record_list[2]
        
    answer = []
    for i in range(len(record)):
        record_list = record[i].split()
        
        if record_list[0] == "Enter":
            answer.append(f"{user_dict[record_list[1]]}님이 들어왔습니다.")
        elif record_list[0] == "Leave":
            answer.append(f"{user_dict[record_list[1]]}님이 나갔습니다.")
    return answer