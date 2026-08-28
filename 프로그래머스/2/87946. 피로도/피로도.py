from itertools import permutations
def solution(k, dungeons):
    answer = -1
    # 현재 피로도가 k
    arr = list(permutations(dungeons , len(dungeons)))
    value_k = k
    for i in arr:
        count = 0
        value_k = k
        for j in i:
            min_value , minus_value = j[0], j[1]
            if value_k < min_value:
                break
            value_k -= minus_value
            count += 1
        answer = max(answer , count)
    return answer