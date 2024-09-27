def solution(record):
    answer = []
    dic = {}
    
    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]
    # print(dic) >> {'uid1234': 'Prodo', 'uid4567': 'Ryan'} 딕셔너리는 같은 키가 여러 번 사용될 수 없음.
    # 이미 존재하는 키에 대해 새로운 값이 들어온 경우, 기존의 값은 새로운 값으로 자동으로 덮어씌워진다. 
    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append(f"{dic[sentence_split[1]]}님이 들어왔습니다.")
        elif sentence_split[0] == 'Leave':
            answer.append(f"{dic[sentence_split[1]]}님이 나갔습니다.")
        
    return answer