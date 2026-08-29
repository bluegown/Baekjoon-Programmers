from itertools import permutations
def solution(ability):
    answer = 0
    x = [i for i in range(len(ability))]
    # 종목의 개수는 len(ability[0])
    # 사람의 수는 len(ability)
    arr = list(permutations(x, len(ability[0])))
    for i in arr:
        count = 0
        sumValue = 0
        for j in i:
            sumValue = sumValue + ability[j][count]
            count += 1
        answer = max(answer, sumValue)
            
        # answer = max(answer , ability[a] + ability[b][1] + ability[c][2])
    return answer