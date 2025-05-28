def solution(a, b, n):
    answer = 0
    while (n // a) >= 1:
        empty = (n // a) * a # 가지고 갈 수 있는 병의 최대 갯수
        n = n - empty
        answer = answer + (empty // a) * b
        n = n + (empty // a) * b

    return answer