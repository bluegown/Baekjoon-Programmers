def solution(my_string):
    answer = ''
    s = list(my_string)
    for i in range(len(s)):
        s[i] = s[i].lower()
    s.sort()
    return ''.join(s)