def solution(n):
    answer = 0
    x = int(n ** (1/2))
    if n == x * x:
        return (x + 1) ** 2
    else:
        return -1
