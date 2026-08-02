import copy
def solution(n, lost, reserve):
    answer = 0
    
    reserve.sort()
    lost.sort()
    rs = copy.deepcopy(reserve)
    for i in rs:
        if i in lost: # 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우
            lost.remove(i)
            reserve.remove(i)
            
    for i in reserve:
        if i-1 in lost: # 에있는 학생에게 빌려주는 경우
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    
            
    
        
        
            
    return n - len(lost)