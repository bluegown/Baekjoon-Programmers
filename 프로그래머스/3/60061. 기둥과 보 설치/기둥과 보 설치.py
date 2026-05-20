def check(arr):
    
    for x,y,a in arr:
        if a == 0: # 기둥
        # 기둥 설치 조건. 해당 좌표에 대한 보가 있거나,
        # 땅바닥에 있어서 0이거나, 
        # 해당 좌표에 기둥이 있는 경우라면 가능함
            if y!= 0 and [x,y-1,0] not in arr and [x-1,y,1] not in arr and [x,y,1] not in arr:
                return False
        else: # 보인 경우
            if [x,y-1,0] not in arr and [x+1, y-1, 0] not in arr and ([x-1,y,1] not in arr or [x+1,y,1] not in arr):
                return False
    return True
            
            
        
def solution(n, build_frame):
    answer = []
    # 기둥과 보...
    
    for x,y,a,b in build_frame:
        if b == 0:
            answer.remove([x,y,a])
            if not check(answer):
                answer.append([x,y,a])
        else:
            answer.append([x,y,a])
            if not check(answer):
                answer.remove([x,y,a])
    answer = sorted(answer, key = lambda x: (x[0], x[1],x[2]))
    return answer
