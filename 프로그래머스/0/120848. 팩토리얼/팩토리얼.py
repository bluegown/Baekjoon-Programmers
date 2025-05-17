def solution(n):
    answer = 1
    value = 1
    if n == 1:
        return 1
    while n > value:
        value = value * answer
        answer += 1 

    answer -= 1 # answer이 하나 더 더해지는것을 방지
    
    if n == value: # 값이 같다면 그냥 리턴해주고
        return answer
    else: # n값이 초과였다면 하나를 더 빼준다
        return answer - 1