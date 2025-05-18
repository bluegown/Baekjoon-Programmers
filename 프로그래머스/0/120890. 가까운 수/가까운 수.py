def solution(array, n):
    answer = 0
    value = 101
    array.sort()
    for i in array:
        if abs(n - i) < value:
            value = abs(n-i)
            answer = i
        
    return answer