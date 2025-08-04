def solution(s):
    answer = True
    stack = []
    value = 0
    if s[0] == ')':
        return False
    
    for i in range(len(s)):
        if value < 0:
            return False
        if s[i] == '(':
            value += 1
        else:
            value -= 1
    
    if value != 0:
        return False
    return True
            
        
            
    
    
    

    return True