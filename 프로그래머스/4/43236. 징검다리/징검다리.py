def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start = 0
    end = distance # 제거해야 하는 바위의 개수를 기점으로 판단해보자
    
    while start <= end:
        mid = (start + end) // 2 # 거리를 기준으로 삼으라고 문제에서 던져준다
        prev_stone = 0
        delete_stone_count = 0 # 삭제할 돌의 갯수
        for rock in rocks:
            if rock - prev_stone < mid: # 둘 사이의 거리가 mid값보다 작다면 삭제 대상 (최솟값중 최댓값을 구해야 한다..)
                delete_stone_count += 1
            else:
                prev_stone = rock

            if delete_stone_count > n:
                break
        if distance - prev_stone < mid:
            delete_stone_count += 1
                
        if delete_stone_count > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
            
        
        
    return answer