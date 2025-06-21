def solution(distance, rocks, n):
    answer = 0
    start , end = 0, distance
    rocks.append(distance)
    rocks.sort()
    
    while start <= end:
        mid = (start + end) // 2
        deleted_stone = 0
        prev_stone = 0
        for idx in rocks:
            if idx - prev_stone < mid: # 만약 이전 돌과의 거리가 mid보다 작다면 제거
                deleted_stone += 1
            else:
                prev_stone = idx # 살아남은 돌
                
            if deleted_stone > n:
                break # 돌이 개수만큼 제거됨
        
        if deleted_stone > n:
            end = mid - 1 # 탐색 범위를 줄인다, 개수가 더 많이 제거된 경우
        else:
            answer = mid
            start = mid + 1
    return answer