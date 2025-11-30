def solution(numbers, hand):
    answer = ''
    left_row, left_col , right_row, right_col = 3,0,3,2
    # left, right 변수는 모두 row, col 기준으로 사용
    arr = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    
    for elements in numbers:
        if elements in [1,4,7]: # [1,4,7]
            left_row = elements // 3 # 0행 , 1행 , 2행
            left_col = 0
            answer += 'L' # 무조건 왼손으로 움직인다
        elif elements in [3,6,9]:  #[3,6,9]
            right_row = (elements -1) // 3 # 0행, 1행, 2행
            right_col = 2
            answer += 'R' # 무조건 오른손으로 움직임
        else: # 왼손 vs 오른쪽 위치를 판별해야 하는 경우
            now_col = 1 # 얘는 가운데니까 1행으로 고정
            if elements in [2,5,8]: # [2,5,8]0열, 1열, 2열
                now_row = (elements) // 3
            elif elements == 0:
                now_row = 3 # 만약 0인 경우는 3열 . 이렇게 현재 위치 지정 완료
                
            left_distance = abs(left_col - now_col) + abs(left_row - now_row)
            right_distance = abs(right_col - now_col) + abs(right_row - now_row)
            if right_distance > left_distance: # 만약 오른쪽 거리가 왼쪽보다 적은 경우 -> 왼손 사용
                left_col = now_col
                left_row = now_row
                answer += 'L'
            elif right_distance < left_distance: # 만약 왼손 거리가 오른쪽보다 적은 경우 -> 오른손 사용
                right_col = now_col
                right_row = now_row
                answer += 'R'
            else: # 만약 둘의 길이가 같은 경우
                if hand == 'right':
                    right_col = now_col
                    right_row = now_row
                    answer += 'R'
                else:
                    left_col = now_col
                    left_row = now_row
                    answer += 'L'
                
            
            
            
    return answer