def solution(fees, records):
    answer = []
    arr = dict()
    fee = dict()
    cars = []
    for i in records:
        time, car_number, io = i.split()
        if car_number not in cars:
            cars.append(car_number)
        print(time, car_number,io)
        if io == 'IN': # 입차라면?
            arr[car_number] = time # 들어간 시간 기록
        if io == 'OUT':
            # 총 몇분인지 계산한다.
            list1 = arr[car_number].split(":")
            hours, minute = int(list1[0]) , int(list1[1])
            list2 = time.split(":")
            hours2, minute2 = int(list2[0]) , int(list2[1]) # 출차시간
            total = (hours2 * 60 + minute2) - (hours * 60 + minute) # 총 시간
            fee[car_number] = fee.get(car_number, 0 ) + total # 차별로 총 머무른 시간
            arr[car_number] = 0
    for key, value in arr.items():
        if value != 0:
            list1 = value.split(":")
            hours, minute = int(list1[0]) , int(list1[1])
            total = (23 * 60 + 59) - (hours * 60 + minute) # 총 시간
            fee[key] = fee.get(key, 0 ) + total # 차별로 총 머무른 시간
    cars.sort()
    print(fee)
    default_time , default_fee , per_time, per_fee = fees[0],fees[1],fees[2],fees[3]
    for car_number in cars:
        if fee[car_number] <= default_time:
            answer.append(default_fee)
        else:
            if (fee[car_number] - default_time) % per_time != 0:
                total_fee = default_fee + ((fee[car_number] - default_time + per_time) // per_time) * per_fee
            else:
                total_fee = default_fee + ((fee[car_number] - default_time) // per_time) * per_fee
            answer.append(total_fee)
            
        


    return answer