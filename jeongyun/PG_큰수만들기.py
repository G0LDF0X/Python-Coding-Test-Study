def solution(number, k):
    answer = ''
    st =[]
    
    for n in number:
        while k > 0 and st and st[-1] < n:
            st.pop()
            k -=1
        st.append(n)
    answer = ''.join(st[:len(st)-k])
    return answer