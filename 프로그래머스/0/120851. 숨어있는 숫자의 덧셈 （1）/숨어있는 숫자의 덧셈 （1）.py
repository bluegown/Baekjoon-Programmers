def solution(my_string):
    answer = 0
    res = [int(i) for i in my_string if i.isdigit()]
    return sum(res)