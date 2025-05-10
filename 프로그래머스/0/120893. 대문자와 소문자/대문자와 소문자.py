def solution(my_string):
    answer = ''
    
    s = list(my_string)
    
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = s[i].lower()
        else:
            s[i] = s[i].upper()

    return ''.join(s)