def solution(n):
    answer = 1
    fac = 1
    if n == 1:
        return 1
    while fac <= n:
        answer += 1 
        fac = fac * answer
        

    answer -= 1 # answer이 하나 더 더해지는것을 방지
    
    return answer