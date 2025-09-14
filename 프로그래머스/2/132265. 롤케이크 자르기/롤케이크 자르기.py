def solution(topping):
    answer = 0
    s = dict()
    
    for i in topping:
        s[i] = s.get(i,0) + 1
    
    s2 = dict()
    
    for i in topping:
        s[i] -= 1 # 수 하나 줄이고
        if s[i] == 0:
            del s[i]
            
        s2[i] = s2.get(i,0) + 1
        if len(s) == len(s2):
            answer += 1
            

    return answer