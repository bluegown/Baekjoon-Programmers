def solution(s):
    answer = True
    s = list(s)
    for i in range(len(s)):
        s[i] = s[i].lower()
    if s.count('p') == s.count('y'):
        return True

    return False