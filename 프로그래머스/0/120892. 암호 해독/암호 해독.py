def solution(cipher, code):
    return cipher[code-1::code] # 시작인덱스 , 끝인덱스(정의안해도됨) , 점프할 수