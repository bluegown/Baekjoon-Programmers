def solution(n):
    answer = 0
    
    for i in range(1,n+1): # 이래야 1부터 n까지 돌아가지
        count = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                count += 1
        if count >= 2:
            answer += 1
        
    return answer