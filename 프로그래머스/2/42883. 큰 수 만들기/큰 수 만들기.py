def solution(number, k):
    answer = ''
    arr = []
    for num in number:
        while k > 0 and arr and arr[-1] < num:
            k -= 1
            arr.pop()
        arr.append(num)
        
    return ''.join(arr[:len(arr) - k])