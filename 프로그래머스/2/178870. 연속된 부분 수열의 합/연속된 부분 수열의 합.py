def solution(sequence, k):
    arr = []
    answer = []
    end = 0
    sumValue = 0
    minValue = 1000000
    N = len(sequence)
    for start in range(N):
        while sumValue < k and end < N:
            sumValue += sequence[end]
            end += 1 # 이러다가 sumValue가 k보다 크거나 같아지면 while문은 멈춘다            
        if sumValue == k:
            arr.append([start,end - 1])
        sumValue -= sequence[start]
        
    for start, end in arr:
        if end - start < minValue:
            minValue = end - start
            answer = [start,end]
    return answer