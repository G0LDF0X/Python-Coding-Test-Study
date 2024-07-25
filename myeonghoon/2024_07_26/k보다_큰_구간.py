# 1 2 3 2 1
# k = 7

# index[0] 부터 [4]까지는 무조건 k보다 클 수 밖에 없다.  배열의 길이 5
# 배열의 길이 5에서 1개 줄인 4가 되는지 확인한다.
# 0-3 = ok, 1-4 = ok, 2-5? 배열의 끝은 4가 끝이기 때문에 얜 안된다. i를 하나씩 증가시켜야겠네
# 배열의 길이 4가 되면 배열의 길이 3도 해본다.
# 0-2 = no, 1-3=no, 2-4=no, 3-5=error / 배열의 길이 3이 전부 실패했으므로 배열이 길이 2는 볼 필요가 없음.


def solution(array, k):
    answer = 0    
    arrary_length = len(array)    
    

    while True:
        if arrary_length < 1:
            break

        i = 0
        j = i + arrary_length
        
        while True:
            total = 0           

            if (j-1) > len(array)-1:                
                break

            for x in range(i, j): # 0 ~ 4, 1 - 5 / 0-3                
                total += array[x]
            if total > k:                
                answer += 1
                    

            i += 1
            j += 1

        arrary_length -= 1

    return answer


array = [1, 2, 3, 2, 1]
k = 7
print(solution(array, k))


array = [1, 1, 1, 1, 1]
k = 2
print(solution(array, k))