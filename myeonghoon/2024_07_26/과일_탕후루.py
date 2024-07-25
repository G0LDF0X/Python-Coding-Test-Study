# 왼쪽부터 1개 빼고, 오른쪽 1개 빼고 번갈아가면서 뺀다.
# 두 종류라는 걸 어떻게 알지?
# 5, 1, 1, 2, 1
# 여기서 index[0]= 5, index[4] = 1이다.
# 앞 포인터는 5를 가르킬거고, 뒤 포인터는 1을 가리킬 거다.
# 왜 투포인터일까?
# 앞 포인터는 어떻게 5를 리스트에서 뽑아낼 수 가 있을까?
# 앞 포인터와 뒤 포인터 사이의 숫자를 조회를 한다.
# 가령 앞 포인터가 5이고, 뒤 포인터가 1이라면 이미 과일이 두 개 꽂혀 있으므로 5,1 이외의 과일이 나온다면 5와 1중 count가 더 적은 과일을 뺀다.
# 5는 count  =1 -> 0
# 1은 count =3
# 2는 count =1
# 그래서 1과 5중에 1이 더 많으므로 5를 제외시킨다.
# 5를 제외시키면 1, 2 이만 남으므로 count 을 모두 더해서 출력

# 1, 1, 1
# 첫번째와 끝은 둘다 1이다.
# 1의 count =3 

# 1 2 3 4 5 6 7 8 9
# 각 숫자마다 count 가 1개씩 존재한다.
# 앞 1 끝 9
# 앞과 뒤의 카운트가 둘 다 동일하면 그냥 앞에서부터 뺀다.
# 최소는 count를 두개를 더 한 값이 2보다 작으면 안됨.

def solution(array):
       
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(len(array)):
        count[array[i]] += 1


    # while True:
    #     # first 가 end와 같거나 end보다 클 시 탐색 종료
    #     if first > end:
    #         break

    #     # 5 카운트 1 증가, 1 카운트 1증가
    #     first_data = array[first] # 5
    #     end_data = array[end] # 1
    #     print(first_data, end_data)

    #     count[first_data] += 1
    #     count[end_data] += 1

    #     first += 1 # 1
    #     end -= 1 # 3


    first = 0
    end = len(array)-1
    # count값 비교
    while True:
        fruit_count = 0
        # 과일의 갯수가 2개 이하이면 종료
        for i in range(len(count)):
            if count[i] > 0:
                fruit_count += 1
        if fruit_count <= 2:
            return sum(count)
            

        # 5 카운트 1 증가, 1 카운트 1증가
        first_data = array[first] # 5
        end_data = array[end] # 1

        if count[first_data] <= count[end_data]: # 1 3
            count[first_data] = 0
            first += 1 # 1
            
        else:
            count[end_data] = 0
            end -= 1 # 3      



array = [5, 1, 1, 2, 1]
print(solution(array))

array1 = [1, 1, 1]
print(solution(array1))

array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(solution(array2))