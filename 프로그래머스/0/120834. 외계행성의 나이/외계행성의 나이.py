def solution(age):
    answer = ''
    s = list(str(age))
    
    for i in range(len(s)):
        s[i] = chr(ord('a') + int(s[i]))
    return ''.join(s)