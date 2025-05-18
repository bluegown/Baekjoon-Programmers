def solution(s):
    answer = ''
    setS = set(s)
    
    for i in setS:
        if s.count(i) == 1:
            answer += i
    answer = sorted(answer)
    
    return ''.join(answer)