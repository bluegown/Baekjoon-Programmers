def solution(n, times):
    answer = 0
    times.sort()
    start = 1
    end = times[-1] * n  # 최댓값
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in times:
            count += mid // i # 평가받을 수 있는 닝겐의 수
        if count >= n: # 더 많이 받고있다면 범위를 줄여야지.
            answer = mid
            end = mid - 1
        else:
            start = mid + 1 
    return answer