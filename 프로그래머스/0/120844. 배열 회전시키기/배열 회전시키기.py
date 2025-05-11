def solution(numbers, direction):

    if direction == 'right':
        answer = [numbers[-1]] + numbers[0:len(numbers) - 1]

    else:
        answer = numbers[1:len(numbers)] + [numbers[0]] 

            
    return answer