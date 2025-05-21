def solution(s):
    answer = 0
    x = s[0]
    same = 0
    diff = 0
    index = -1
    for i in range(len(s)):
        if x == s[i]: # 만약 같은 수라면
            same += 1
        else:
            diff += 1
        
        if same == diff: 
            answer += 1
            same = 0
            diff = 0
            if i == len(s) - 1:
                continue
            else:
                x = s[i+1]
        
    if same != diff:
        answer += 1
    return answer