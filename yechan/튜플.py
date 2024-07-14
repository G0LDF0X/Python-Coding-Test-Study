def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s = sorted(s, key=lambda x: len(x))
    print (s)
    for i in range(len(s)):
        s[i] = s[i].split(",")
        for j in range(len(s[i])):
            s[i][j] = int(s[i][j])
    print(s)
    answer.append(s[0][0])
    for i in range(1, len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in s[i-1]:
                answer.append(s[i][j])
                break

    return answer
# 모르겠어요... ㅠㅠ