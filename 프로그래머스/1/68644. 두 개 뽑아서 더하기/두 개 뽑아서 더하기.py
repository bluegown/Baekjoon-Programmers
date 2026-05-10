from itertools import combinations
def solution(numbers):
    answer = []
    arr = list(combinations(numbers, 2))
    res = set()
    
    for i in arr:
        x = i[0] + i[1]
        if x not in res:
            res.add(x)
    answer = sorted(res)
    return answer