def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    for i in range(0,len(score),m):
        arr = score[i:i+m]
        if len(arr) < m:
            continue # 남는 사과들이므로 그냥 버림
        answer += min(arr) * m # min(arr) -> p
    return answer