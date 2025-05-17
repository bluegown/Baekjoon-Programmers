def solution(emergency):
    answer = []
    emg = sorted(emergency) # 3,24, 76
    
    for i in emergency:
        answer.append(len(emergency ) - emg.index(i))
    
    
    return answer