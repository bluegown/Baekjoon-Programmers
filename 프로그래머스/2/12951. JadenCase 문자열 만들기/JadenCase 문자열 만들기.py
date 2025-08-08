def solution(s):
    s_low = s.lower()
    arr = list(s_low.split(' '))
    for i in range(len(arr)):
            if arr[i] == '':
                continue
            if arr[i][0].isalpha():
                arr[i] = arr[i][0].upper() + arr[i][1:].lower()

    
    return ' '.join(arr)
