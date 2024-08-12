def solution(want, number, discount):
    from collections import Counter

    # 원하는 제품과 수량을 딕셔너리로 변환
    want_dict = dict(zip(want, number))
    
    # 할인 제품의 길이
    discount_length = len(discount)
    
    # 10일 동안의 할인 제품을 카운트할 딕셔너리
    current_count = Counter()
    
    # 결과 카운트
    valid_start_days = 0
    
    # 슬라이딩 윈도우를 사용하여 10일 동안의 할인 제품을 확인
    for i in range(discount_length):
        # 현재 제품을 추가
        current_count[discount[i]] += 1
        
        # 윈도우 크기가 10이 되면
        if i >= 9:
            # 윈도우의 시작 인덱스
            start_index = i - 9
            
            # 원하는 제품이 모두 충족되는지 확인
            if all(current_count[want_item] >= want_dict[want_item] for want_item in want):
                valid_start_days += 1
            
            # 윈도우의 시작 제품을 제거
            current_count[discount[start_index]] -= 1
            if current_count[discount[start_index]] == 0:
                del current_count[discount[start_index]]
    
    return valid_start_days
