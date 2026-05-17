def solution(numbers, hand):
    result = ''
    left_number = {1,4,7}
    right_number = {3,6,9}
    left = [3,0]
    right= [3,2] # 행 / 열
    
    for i in range(len(numbers)):
        if  numbers[i] in left_number:
            result += 'L'
            left = [(numbers[i] - 1) // 3 , 0]
        elif numbers[i] in right_number:
            result += 'R'
            right = [(numbers[i]  - 3) // 3 , 2]
        else:
            # 2,5,8,0에 위치한 경우, col은 1로 고정
            if numbers[i]  == 0:
                row = 3
            else:
                row = (numbers[i]  - 2) // 3 
            col = 1
            if abs(left[0] - row) + abs(left[1] - col) < abs(right[0] - row) + abs(right[1] - col):
                result += 'L'
                left = [row, col]
            elif abs(left[0] - row) + abs(left[1] - col) > abs(right[0] - row) + abs(right[1] - col):
                result += 'R'
                right = [row, col]
            else:
                if hand == 'right':
                    result += 'R'
                    right = [row, col]
                else:
                    result += 'L'
                    left = [row, col]
    return result