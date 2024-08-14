def solution(n, t, m, p):
    answer = ''
    tube = []
    
    # 튜브가 말해야되는 숫자가 몇번째 숫자인지를 저장. p 번째로 시작 , m명이서 게임. m명이서 총 t번의 게임을 해야됨. 
    for i in range(t):
        tube.append(p + m * i)
        
    #print(tube)

    arr = []    # n진수로 바꿔서 말해야 될 배열을 쭉 계산한 것 
    i = 0
    # arr의 길이가 튜브가 말해야 될 그 x번째 수가 될때까지 반복 
    while len(arr)<= tube[t-1]:
        tmp = convert_to_n(n, i)    # i를 n진수로 변환
        arr.extend(tmp)     # tmp 를 각 자릿수마다 arr에 저장, tmp = '12' 이면 '1', '2' 이렇게 arr에 저장함.
        i +=1
    # print(arr)
    
    # 튜브가 말해야될 i번째 숫자는 뭔지 arr에서 찾아서 answer 에 저장 
    for i in tube:
        answer += arr[i-1]
    return answer

# n 진수로 변환하는 함수 
def convert_to_n(n, num):
    digits = "0123456789ABCDEF"     # 변환한 수에 사용되는 문자 모음 
    arr = []
    
    if num == 0:
        return "0"
    
    # num을 계속 나누어서 나머지를 arr에 저장 -> n 진수로 변환 
    while num > 0:
        arr.append(digits[num % n])
        num //=n
                   
                
    return ''.join(reversed(arr))   # arr를 역순으로 리턴 