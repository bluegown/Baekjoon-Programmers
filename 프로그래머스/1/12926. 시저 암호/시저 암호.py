def solution(s, n):
    answer = ''
    
    for i in s:
            if i == ' ':
                answer += ' '
            elif 'a' <= i <= 'z' and ord(i) + n > ord('z'): # 만약 z를 넘어가는 경우
                index = ord(i) + n - ord('z')
                answer += chr(ord('a') + index - 1)
            elif 'A' <= i <= 'Z' and ord(i) + n > ord('Z'): # 만약 z를 넘어가는 경우
                index = ord(i) + n - ord('Z')
                answer += chr(ord('A') + index - 1)  
            else:
                answer += chr(ord(i) + n)
    return answer