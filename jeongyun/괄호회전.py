def solution(s):
    answer = -1

    # right(s)
    for i in range(len(s)):
        new_s = ""
        new_s = s[i:] + s[:i]
        # print(new_s)
        if right(new_s) == True:
            answer +=1
    return answer+1

def right(s):
    st = []
    for i in s:
        if len(st) == 0:
            st.append(i)
        else:
            if st[-1]== '(' and i == ')':
                st.pop()
            elif st[-1]=='{' and i == '}':
                st.pop()
            elif st[-1]=='[' and i == ']':
                st.pop()
            else:
                st.append(i)
    if len(st) == 0:
        return True
    else:
        return False
    
    