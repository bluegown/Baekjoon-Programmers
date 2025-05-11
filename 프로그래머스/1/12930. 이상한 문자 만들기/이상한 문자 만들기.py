def solution(s):
    s = list(s)
    index = 1
    for i in range(len(s)):
        if s[i] == ' ':
            index = 1
            continue
        if index % 2 == 1:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
        index += 1

    
    return ''.join(s)