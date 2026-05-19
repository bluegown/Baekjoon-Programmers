def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length    # 다리
    sum_bridge = sum(bridge)          # 무게. 초기에는 0으로 시작
    answer = 0                      

    while bridge:
        answer += 1
        sum_bridge -= bridge.pop(0) # 맨 앞에 위치한 트럭이 다리를 지나면 하중 감소

        # 남은 대기 트럭이 있는 경우 
        if truck_weights:
            # 견딜 수 있는 무게?
            if sum_bridge + truck_weights[0] <= weight:
                new_truck = truck_weights.pop(0)    # 대기 트럭에서 출발
                bridge.append(new_truck)            # 다리에 새로운 트럭 추가
                sum_bridge += new_truck               # 새로운 트럭만큼 다리 하중 증가
            else:
                bridge.append(0)                    # 다리에 0을 추가해 자리 이동 표시
    return answer