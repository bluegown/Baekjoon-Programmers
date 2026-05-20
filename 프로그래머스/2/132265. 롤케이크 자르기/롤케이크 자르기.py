def solution(topping):
    answer = 0
    s1 = dict()
    s2 = dict()
    for i in topping:
        s1[i] = s1.get(i, 0 ) + 1
    for i in topping:
        s1[i] -= 1
        if s1[i] == 0:
            del s1[i]
        
        s2[i] = s2.get(i,0) + 1
        if len(s1) == len(s2):
            answer += 1
    return answer