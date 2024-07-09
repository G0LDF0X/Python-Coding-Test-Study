def solution(citations):
    answer = 0
    citations2 = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if(citations2[i] != 0):
            if (i+1==citations2[i] ):
                answer=i+1
                return answer
            elif (i+1>citations2[i]):
                answer=i
                return answer
            else:
                answer=len(citations)
    return answer