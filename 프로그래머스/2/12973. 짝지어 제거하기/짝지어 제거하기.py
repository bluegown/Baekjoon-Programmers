def solution(s):
    answer = -1
    stack = []
    stack.append(s[0])
    if len(s) == 1:
        return 0
    
    for i in range(1,len(s)):
        stack.append(s[i])
        if len(stack) >= 2: # 만약 길이가 2가 넘는다면 keep going
            if stack[-1] == stack[-2]: # 최상단 원소 2개가 같은 경우
                stack.pop()
                stack.pop()
        #길이가 1이라면? Do nothing
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer