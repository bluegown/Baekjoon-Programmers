def solution(cipher, code):
    answer = ''
    for i in range(1,len(cipher) + 1):
        if (code * i) - 1 >= len(cipher):
            break
        answer += cipher[(code * i) - 1]
    return answer