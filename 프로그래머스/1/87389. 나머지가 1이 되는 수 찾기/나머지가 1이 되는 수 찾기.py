def solution(n):
    answer = 0
    for x in range(2, n + 1):
        if n % x == 1:
            return x
    return n - 1