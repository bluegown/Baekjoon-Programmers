def solution(participant, completion):
    answer = ''
    ans = dict()
    for i in participant:
        ans[i] = ans.get(i,0) + 1
    for j in completion:
        ans[j] -= 1
    for i in ans:
        if ans[i]:
            return i
    return answer