def solution(lottos, win_nums):
    answer = []
    maxValue = 0
    minValue = 0
    for i in lottos:
        if i in win_nums:
            maxValue += 1
            minValue += 1 # 100% 일치하는 것은 일단 포함시킨다
        
    for i in lottos:
        if i == 0:
            maxValue += 1
    maxRank = 6
    minRank = 6
    if maxValue >= 2:
        maxRank = 7 - maxValue
    if minValue >= 2:
        minRank = 7 - minValue
        
    
    
    return [maxRank,minRank]