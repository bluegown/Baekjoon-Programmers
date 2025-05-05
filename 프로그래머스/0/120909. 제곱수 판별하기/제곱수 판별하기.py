import math
def solution(n):
    answer = 0
    num = int(math.sqrt(n))
    if num * num == n:
        answer = 1
    else:
        answer = 2
    return answer