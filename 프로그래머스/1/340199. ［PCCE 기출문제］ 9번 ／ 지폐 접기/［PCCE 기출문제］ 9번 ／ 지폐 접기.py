def solution(wallet, bill):
    answer = 0
    # '항상' 길이가 긴쪽을 절반으로 줄인다
    # // 2로 길이 줄이기ㅣ
    # 그대로 or 90도 회전 -> 조건 충족
    
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        answer += 1
    return answer