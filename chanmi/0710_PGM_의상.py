def solution(clothes):
    # [의상의 이름, 의상의 종류]
    clothes_dict = {}
    for cloth in clothes:
        # 뒤쪽에 있는 의상의 종류가 이미 dict에 있는 경우
        if cloth[1] in clothes_dict:
            # 해당 종류에 의상 추가
            clothes_dict[cloth[1]].append(cloth[0])
        else:
            # 처음 보는 의상 종류일 경우
            clothes_dict[cloth[1]] = [cloth[0]]
    
    # 각 의상 별로 선택할 수 있는 경우의 수는
    # [의상1, 의상2, ..., 입지 않는다] 같은 느낌이므로
    # 각 의상 종류별의 의상에 1을 더한 값을 모두 곱한 후 전부 입지 않는 경우인 1을 빼면 된다.

    answer = 1
    for key in clothes_dict.keys():
        answer *= (len(clothes_dict[key]) + 1)
    return answer - 1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) # 5

# headgear에 yellow_hat, green_turban이 있음
# eyewear에 blue_sunglasses가 있음

# headgear, eyewear에서 반드시 하나는 입어야 하므로
# 1. yellow_hat(headgear)
# 2. green_turban(headgear)
# 3. blue_sunglasses(eyewear)
# 4. yellow_hat(headgear) + blue_sunglasses(eyewear)
# 5. green_turban(headgear) + blue_sunglasses(eyewear)
# 로 총 5개의 조합이 된다.

# dictionary를 이용해 각 의상을 종류별로 dict 변수 내에 저장하면 될 것 같다.