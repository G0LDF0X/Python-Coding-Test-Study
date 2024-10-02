def solution(price, money, count):
    answer = -1
    sum = 0
    for idx in range(1, count+1):
        amusement_park_price = price * idx
        sum += amusement_park_price
    if sum - money < 0:
        answer = 0
    else:
        answer = sum - money 
    return answer

price = 3
money = 20
count = 4
print(solution(price, money, count))

# 가격이 3인 놀이기구를 4번 타겠다는 것임
# 3(price*idx) + 6 + 9 + 12 = 총 30
# 돈은 20밖에 없으므로 10을 반환
# 만약 금액이 부족하지 않다면(sum - money < 0) 0을 반환