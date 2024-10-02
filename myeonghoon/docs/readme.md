## 덧칠하기
```
def solution(n, m, section):
    answer = 0
    i = 0 # 인덱스 위치    
    while i<len(section):      
        roller_start = section[i]       
        roller_end = (m + roller_start)-1

        if roller_end > n:
            over = roller_end - n # 무조건 양수
            roller_start -= over
            roller_end -= over        
        print("롤러: ", roller_start, "부터", roller_end, "까지")
        
        while roller_start <= section[i] <= roller_end and i<len(section):           
            print("페인드로 덮인 섹션 : ", section[i])
            i += 1               

        answer += 1
        print("페인트 칠 횟수 : ", answer)             
        
    return answer
```

#### 오류 발생
```
while roller_start <= section[i] <= roller_end and i<len(section):            
    print("페인드로 덮인 섹션 : ", section[i])
    i += 1 
```

### 예시
```
n = 8 # 벽
m = 4 # 롤러 길이
section = [2, 3, 6] # 페인트 칠해야 되는 벽
```

너무나도 신기했던 오류이다. 전혀 생각지도 못했다.
그러나 이유는 간단했다. 롤러로 벽을 계속 칠하다보면 i의 위치는 어느새 마지막 인덱스에
가 있게 된다(예시에서 section의 마지막 위치는 2이다). 그 상태에서 i += 1을 해주면
i는 3이므로 인덱스의 범위에서 벗어나게 된다. 따라서 조건을 설정해줘야 하는데 
```
while roller_start <= section[i] <= roller_end and i<len(section)
```
에서 롤러의 범위 안에 없거나 section리스트의 범위 안에 있지 안으면 while문을 들어갈 수 없다.
하지만 문제는 `i<len(section)`조건이 `section[i]`뒤에 있다는 것이다. 원래라면 `i<len(section)`조건을 먼저 실행하여 범위에 벗어난 값이 `section[i]`조건 안에 들어가는 것을
막아야 한다. 하지만 `section[i]`조건문을 먼저 뒀기 때문에 인덱스 에러가 발생했다.


