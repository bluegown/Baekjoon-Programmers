def solution(land):
    answer = 0
    dp = [[0 for _ in range (len(land[0]))] for _ in range(len(land))]
    
    for i in range(len(land[0])):
        dp[0][i] = land[0][i] # 초기값 세팅
        
    for i in range(1, len(land)):
        for j in range(4):
            if j == 0:
                dp[i][j] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][j]
            if j == 1:
                dp[i][j] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][j]
            if j == 2:
                dp[i][j] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][j]
            if j == 3:
                dp[i][j] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][j]
            
            
        
            
        
    

    return max(dp[-1])