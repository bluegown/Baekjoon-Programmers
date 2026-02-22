from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
    
    # 이렇게 하면 location , value로 queue가 구성됨
    while queue:
        index, value = queue.popleft() # index, 우선순위
        if not queue:
            return answer + 1
        
        if value >= max(x[1] for x in queue): # 남아있는 값보다 전부 큰 경우. 그대로 빼고 넘어간다.
            answer += 1
            if index == location:
                return answer
            else:
                continue
        else: # value = max()니까, 
            queue.append((index, value))
            
        print(queue)
    
    return answer