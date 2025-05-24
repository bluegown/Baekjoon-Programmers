def solution(s):
    answer = []
    dic = dict()
    index = 0
    for i in range(len(s)):
        index = 0
        if s[i] not in dic:
            answer.append(-1) # 없는경우
            dic[s[i]] = i
        else:
            for j in range(i):
                if s[j] == s[i]:
                    index = j
            answer.append(i - index)
            
    
    return answer