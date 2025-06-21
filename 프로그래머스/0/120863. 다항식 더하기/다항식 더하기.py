def solution(polynomial):
    answer = ''
    arr = polynomial.split("+")
    for i in range(len(arr)):
        arr[i] = arr[i].replace(" ",'')

    one = 0
    const = 0
    for i in range(len(arr)):
        if 'x' in arr[i]:
            if len(arr[i]) == 1:
                one += 1 # 계수가 1인 경우 (x)
            elif len(arr[i]) == 2:
                one += int(arr[i][0]) # 2x , 3x , 4x..9x
            elif len(arr[i]) == 3:
                one = one + int(arr[i][0]) * 10
                one = one + int(arr[i][1])
        else:
            const += int(arr[i])
    
    if one == 1:
        answer += 'x' # 1인경우 x만 
    elif one > 1:
        answer += str(one) + 'x' # 2가 넘는다면 
        
    
    if const != 0:
        if one != 0:
            answer += ' + '
            
        answer += str(const)
            
    print(answer)
    return answer