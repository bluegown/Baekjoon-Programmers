def solution(name):
    answer = 0
    size = len(name)
    min_move = size - 1
    for index , value in enumerate(name):
        answer += min(ord(value) - ord('A') , ord('Z') - ord(value) + 1) # 스틱의 좌우
        
        next_index = index + 1
        while next_index < size and name[next_index] == 'A': # 연속된 A구간을 구하고, 그게 단절되는 구간을 구한다
            next_index += 1
        min_move = min(min_move, 2 * index + (size - next_index) , 2 * (size - next_index) + index)
        
    answer += min_move
    return answer