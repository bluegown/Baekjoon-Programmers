def solution(order):
    s = list(str(order))
    answer = 0
    for i in s:
        if int(i) in set([3,6,9]):
            answer += 1
    return answer