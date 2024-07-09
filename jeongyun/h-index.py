def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse = True)
    
    for i in range(n, 0, -1):
        h = 0
        for c in citations:
            if c >= i:
                h +=1
                #print(i,c,h)
            else:
                break
        #print(h, i)
        if h >= i:
            # print(h, i)
            answer = i
            break
        if h == n:
            answer = h
            break
    return answer