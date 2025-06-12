def solution(numbers):
    answer = 0
    dic = set()
    
    for i in range(10):
        dic.add(i)

    for i in dic:
        if i not in numbers:
            answer += i
    return answer