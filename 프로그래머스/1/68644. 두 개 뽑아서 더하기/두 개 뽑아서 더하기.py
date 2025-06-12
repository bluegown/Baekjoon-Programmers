from itertools import combinations
def solution(numbers):
    answer = []
    ans = list(combinations(numbers,2))

    for i in ans:
        if (i[0] + i[1]) not in answer:
            answer.append(i[0] + i[1])

    answer.sort()
    return answer