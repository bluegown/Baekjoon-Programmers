def solution(N, number):
    answer = -1
    dp = [set() for _ in range(9)] # N의 범위가 1부터 9 사이에 위치
    
    for i in range(1, 9):
        arr = dp[i]
        arr.add(int(str(N) * i)) # 555, 55와 같음
        
        for j in range(1, i ):
            for k in dp[j]: # 현재까지 계산해온 dp배열에 대해 확인
                for m in dp[i - j]:
                    arr.add(k + m)
                    arr.add(k - m)
                    arr.add(k * m)
                    if m!= 0 and k!=0:
                        arr.add(k // m)
        if number in arr:
            return i
    
    return answer