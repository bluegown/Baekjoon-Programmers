def solution(money):
    answer = 0
    dp = [0] * len(money)
    dp[0] = money[0] # 0번 턴경우 -> 2번부터 가능함
    dp[1] = money[0]
    
    dp2 = [0] * len(money) # 0번 안털고 가는경우
    dp2[0] = 0 # 1번부터 갈 수 있어요 !!
    dp2[1] = money[1]
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
        
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(max(dp), max(dp2))