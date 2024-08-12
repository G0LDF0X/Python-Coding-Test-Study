def solution(want, number, discount):
    answer = 0
    arr = []
    n = len(discount)
    market = []
    
    for i in range(len(number)):
        for j in range(number[i]):
            arr.append(want[i])    
    # print(arr)
    for i in range(n - 10 + 1):
        market = discount[i:i+10]
        # print(market)
        for j in range(10):
            # print(arr[j], market)
            if arr[j] in market:
                idx = market.index(arr[j])
                del market[idx]
        if len(market) == 0:
            answer +=1
    return answer