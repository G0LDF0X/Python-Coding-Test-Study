def solution(clothes):
    answer = 0
    return answer

# 실패
def hash(clothes):
    # key값 먼저 찾기
    hash_table = {}

    # key['headgear'] 
    for i in range(len(clothes)):
        if clothes[i][1] in hash_table:
            hash_table[clothes[i][1]].append(clothes[i][0])
        else:
            hash_table[clothes[i][1]] = [clothes[i][0]]
    # value값 찾기 
    print(hash_table['eyewear'])

# 
def test_1(clothes):
    count =0 
    for i in range(len(clothes)):
        count += 1
    print(count)    

# 헤드기어 3
# 

clothes_1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]] # 최대 7가지
clothes_2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]] # 7가지

# test_1(clothes_1)
hash(clothes_1)

# headgear/ eyewear / headgear / headgear, eyewear / headgear, headgear / headgear, eyewear / headgear, eyewear, headgear /
# 위에 이거 완전탐색 아님....

# 동일 부위 중복 착용 불가
# 키를 이용해서 value 값을 조회할 수 있어야 한다.
# 만약 이미 키 값이 존재한다면 존재하는 키 안에 value 값을 추가해야 한다.


# 전체를 조회하면서 규칙을 찾아라
# 규칙이 안보이는데.....
# 옷의 종류가 3가지 부위가 2개
# 머리 : 노란 모자를 착용한다 +1
# 
# 3cr = 3*3*2
# 콤비네이션?

# 완전 탐색 다시 해보기


# < yellow_hat과 blue_sunglasses 조합 >모자 1개, 상의 1개의 조합의 수 : (4-1)개
# 의상 2개, 모자 1개, 상의 1개 -> 
# yellow_hat만 착용한다
# blue_sunglasses만 착용한다
# 모두 착용한다.
# 모두 착용하지 않는다. x

# < blue_sunglasses, green_turban >모자 2개, 상의 1개의 조합의 수 : (8- 3)= 5개
# 의상 3개, 의상 종류 2개(모자 2개, 상의 1) = 의상 종류 3개 + 
# yellow_hat만
# blue_sunglasses 착용
# green_turban 쓴다
# blue_sunglasses, green_turban 착용 
# yellow_hat, blue_sunglasses 착용
# yellow_hat, blue_sunglasses, green_turban 착용 x (모자 2개 조합이라서)
# yellow_hat, green_turban 착용 x (모자 2개 조합이라서)
# 아무것도 착용하지 않는다 x


# ["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"] 
# 모자 3개일 때 조합의 수 : (4-1)= 3가지 ->의상종류 3개 +1 -1
# 의상 3개, 모자 1개 -> (3 * 1)+1 -1 , 
# crow_mask착용
# blue_sunglasses착용
# smoky_makeup 착용
# 모두 착용 안함 x

# test 1 (의상 * 의상 종류)+1 -1 -> (3, 6)x
# test 2 (의상)