import math
def solution(n):
    answer = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            answer += 2
            if i == (n // i):
                answer -= 1
        
    return answer