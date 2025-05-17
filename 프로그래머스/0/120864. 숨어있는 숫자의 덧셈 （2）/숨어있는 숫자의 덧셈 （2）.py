def solution(my_string):
    answer = 0
    temp = False
    value = 1
    
    reversed_string = my_string[::-1]
    for i in reversed_string:
        if i.isdigit():
            temp = True
            answer += int(i) * value # value는 자리수
            value = value * 10
        else:
            value = 1
            temp = False
            
    return answer