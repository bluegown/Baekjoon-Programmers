from bisect import bisect_right
from bisect import bisect_left
def solution(N, stages):
    answer = []
    arr = [0] * (N + 1)
    stages.sort()
    
    for index in range(1,N+1): # N: 1~ 500
        firstIndex = bisect_left(stages,index)
        lastIndex = bisect_right(stages,index)

        if len(stages) == firstIndex:
            continue
        arr[index] = (lastIndex - firstIndex) / (len(stages) - firstIndex)
            
    valueArray = []
    for i in range(1,len(arr)):
        valueArray.append((i,arr[i]))
    
    print(valueArray)
    valueArray = sorted(valueArray, key = lambda x:(-x[1],x[0]))
    print(valueArray)
    
    for i in range(len(valueArray)):
        answer.append(valueArray[i][0])
        
    return answer