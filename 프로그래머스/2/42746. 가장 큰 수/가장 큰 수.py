def solution(numbers):
    answer = ''
    
    num = [str(x) for x in numbers]
    num.sort(key = lambda x: x * 3,reverse = True)
    answer = ''.join(num)
    
    

    return str(int(answer))