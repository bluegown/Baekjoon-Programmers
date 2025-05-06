def solution(my_string):
    answer = ''
    q = {'a','e','i','o','u'}
    for i in my_string:
        if i not in q:
            answer += i
    return answer