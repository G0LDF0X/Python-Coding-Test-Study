from math import ceil

def solution(fees, records):
    answer = []
    parking = {}    # 주차 기록 저장할 딕셔너리 {'차량번호' : ['총 주차 시간', '마지막 입/출차 시각', '입/출차']}
    base_time = fees[0] # 기본 시간
    base_fee = fees[1]  # 기본 요금
    unit_time = fees[2]  # 단위 시간
    unit_fee = fees[3]  # 단위 요금 
    
    for i in range(len(records)):
        park_hour = int(records[i][:2])
        park_min = int(records[i][3:5])
        park_at = 60 * park_hour + park_min # 입/출차 시각 
        car = records[i][6:10]  # 차량 번호
        io = records[i][-3:]    # 입 출차
        park_time = 0

        # car 가 이미 딕셔너리에 있는 경우 
        if car in parking:
            # out 이면 주차시간 계산해서 저장 
            if io== 'OUT' :
                park_time = park_at - parking[car][1]
                parking[car][0] += park_time 
                parking[car][1] = 0
                parking[car][2] = io
            # in 이면 park_at 업데이트 
            else:
                parking[car][1] = park_at
                parking[car][2] = io
        # car 가 딕셔너리에 없으면 초기화 
        else:
            parking[car] = [park_time, park_at, io]
        
        
    # in 기록만 있고 out 기록 없는 자동차 23:59 분에 out처리 
    for car in parking:
        if parking[car][2] == ' IN' :
            parking[car][0] += (23*60+59) - parking[car][1]
            parking[car][2] = 'OUT'
            

    # 차량번호대로 정렬
    sorted_parking = dict(sorted(parking.items()))

    # 주차 요금 계산 ( 기본요금 + 단위요금 )
    for car in sorted_parking:
        fee = base_fee
        if parking[car][0] < base_time:
            answer.append(fee)
        else:
            fee += ceil((parking[car][0]-base_time) / unit_time) * unit_fee 
            answer.append(fee)
            
    return answer