def check_right_str(st):
    ans = 0
    for i in range(len(st)):
        if st[i] == '(':
            ans += 1
        else:
            ans -= 1
        if ans < 0:
            return False
    if ans == 0:
        return True
    else:
        return False

def divide_str(st):
    index = 0
    ans = 0
    for i in range(len(st)):
        if st[i] == '(':
            ans += 1
        if st[i] == ')':
            ans -= 1
        if ans == 0:
            index = i
            break
    u,v = ''.join(st[:index + 1]) , ''.join(st[index+1:]) # 0 ~ index, index +1 ~
    return u,v
def solution(p):
    answer = ''
    if len(p) == 0:
        return ''; # 1번 조건
    
    if check_right_str(p): # 이미 올바른 괄호 문자열이라면 ?
        return p
    u,v = divide_str(p) # 2번 조건
    if check_right_str(u):
        answer = u + solution(v) # v를 가지고 1번부터 재수행한다
    else:
        answer = '('
        answer = answer + solution(v)
        answer += ')'
        u = list(u)
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == ')':
                u[i] = '('
            else:
                u[i] = ')'
        answer = answer + ''.join(u)
        
    return answer