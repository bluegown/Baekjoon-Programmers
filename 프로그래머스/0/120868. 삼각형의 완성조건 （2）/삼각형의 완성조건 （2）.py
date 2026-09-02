def solution(sides):
    answer = 0
    # 1. 가장 큰 변인 경우
    # 두개의 합보다 작아야 하고
    # 2 . 가장 큰 변이 아닌 경우
    # min(sides) + a > max(sides)
    a = sum(sides) # 이거보다 작아야 한다
    b = max(sides) - min(sides) # 이거보단 커야하고
    for i in range(b  + 1, a):
        answer += 1
    
    return answer