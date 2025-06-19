from itertools import combinations
def solution(numbers):
    answer = []
    co = list(combinations(numbers,2))
    for i in co:
        if i[0] + i[1] not in answer:
            answer.append(i[0] + i[1])
    answer.sort()
    return answer