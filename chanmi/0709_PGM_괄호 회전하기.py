def solution(s):
    s = list(s)
    brackets_pair = {"(":")", "{":"}", "[":"]"}
    count = 0
    for i in range(len(s)):
        print("사전체크", s)
        stack = []
        if i != 0:
            stack = s[i:] + s[:i]
        else:
            stack = s[:]
        
        store = []
        # 짝이 안 맞는지 확인하는 용도
        is_break = False
        print("체크", stack)
        while len(stack) != 0:
            bracket = stack.pop()
            # 맨 끝이 {거나 (거나 [인 경우
            if bracket in brackets_pair:
                if len(store) != 0 and brackets_pair[bracket] == store[-1]:
                    store.pop()
                else:
                    is_break = True
                    break
            # 그냥 }, ), ]인 경우
            else:
                store.append(bracket)
        
        # 짝이 안 맞는 경우 없이 while문을 다 돌았을 경우
        if not is_break and len(store) == 0:
            count += 1
            print("통과")
        else:
            print("실패")
    return count

solution("}}}") # 0
