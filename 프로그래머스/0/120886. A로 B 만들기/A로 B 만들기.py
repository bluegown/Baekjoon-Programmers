def solution(before, after):
    answer = 0
    bf = {}
    af = {}
    for i in before:
        if i not in bf:
            bf[i] = 1
        else:
            bf[i] += 1
    
    for i in after:
        if i not in af:
            af[i] = 1
        else:
            af[i] += 1
    if bf == af:
        answer = 1
    else:
        answer = 0
    return answer