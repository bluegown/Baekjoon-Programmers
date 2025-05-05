def solution(s1, s2):
    answer = 0
    s1 = set(s1)
    s2 = set(s2)
    
    for i in s1:
        if i in s2:
            answer += 1
    return answer