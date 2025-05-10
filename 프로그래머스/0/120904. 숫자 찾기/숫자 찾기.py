def solution(num, k):
    answer = 0
    s = list(str(num))
    print(s)
    if str(k) in set(s):
        return s.index(str(k)) + 1
    return -1