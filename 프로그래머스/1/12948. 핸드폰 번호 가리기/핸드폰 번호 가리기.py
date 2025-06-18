def solution(phone_number):
    answer = []
    
    length = len(phone_number) - 4
    
    answer = ['*' * length]
    number = phone_number[-4:]
    ans = ''.join(answer) + ''.join(number)
    return ans