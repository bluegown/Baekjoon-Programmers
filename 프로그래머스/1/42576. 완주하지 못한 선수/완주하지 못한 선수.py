def solution(participant, completion):
    answer = ''
    ans = dict()
    for i in participant:
        ans[i] = ans.get(i,0) + 1
    for i in completion:
        ans[i] -= 1
    for key, value in ans.items():
        if value == 1:
            return key
    return answer