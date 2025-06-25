def solution(participant, completion):
    answer = ''
    par = dict()
    com = dict()
    for i in range(len(participant)):
        if participant[i] in par:
            par[participant[i]] += 1
        else:
            par[participant[i]] = 1
    for i in range(len(completion)):
        if completion[i] in par:
            par[completion[i]] -= 1
    
    for i in par.items():
        if i[1] == 1:
            return i[0]
    
    return answer