def solution(msg):
    answer = []
    n = len(msg)
    LZW = [chr(i) for i in range(65, 91)]   # 'A', 'B', 'C', ..., 'Z' 아스키코드 이용해서 만드는 방식
    # print(LZW)
    
    for _ in range(n):
        idx = 0
        # print(msg)
        for i in range(1, len(msg)+1):
            if msg[:i] in LZW:     # LZW에 있는 경우 -> 단어가 LZW에 없을때까지 반복 
                idx = LZW.index(msg[:i])
                # print(msg[:i], idx+1)
            else:       # LZW 에 없는 경우 
                # print(msg[:i], idx, "1")
                
                # LZW 에 해당 단어 추가 
                LZW.append(msg[:i])
                # print(LZW[-1])
                
                # 저장된 idx 값 answer 에 저장 (직전문자까지로 LZW에 있는 인덱스 값 )
                answer.append(idx+1)
                
                # msg 에서 이미 찾은 단어 삭제 
                msg = msg[i-1:]
                # print(msg, '---')
                break
            
    # 마지막 문자 인덱스 저장 
    answer.append(idx+1)
    
    return answer