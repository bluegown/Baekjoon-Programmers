def solution(n):
    # 1 ~ 7 1 , 8~ 14 2. 15 ~ 21 3, 22 ~ 28 4 이런식으로 간다
    if n % 7 == 0:
        return n // 7
    return n // 7 + 1