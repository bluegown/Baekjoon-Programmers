from collections import deque
def solution(progresses, speeds):
    answer = []
    prev_day = (100 - progresses[0]) // speeds[0]
    if (100 - progresses[0]) % speeds[0] != 0:
        prev_day += 1
    count = 1
    for i in range(1, len(progresses)):
        newDay = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            newDay += 1
        if newDay <= prev_day: # 앞의 작업보다 빨리 끝나는 경우
            count += 1
        else:
            prev_day = newDay # 앞의 작업보다 늦게 끝나는 경우 
            answer.append(count)
            count = 1
            
    if count != 0:
        answer.append(count)
            
            
        

    
    
            
        
                
            
            
        
        
        
    return answer