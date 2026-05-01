def solution(clothes):
    answer = 1
    arr = dict() 
    for name, value in clothes:
        arr[value] = arr.get(value, 0) + 1
    for key, value in arr.items():
        answer *= (value + 1)
    return answer - 1