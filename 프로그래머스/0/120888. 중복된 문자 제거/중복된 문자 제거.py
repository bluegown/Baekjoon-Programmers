def solution(my_string):
    answer = []
    for i in my_string:
        if i not in set(answer):
            answer.append(i)
            
    return ''.join(answer)