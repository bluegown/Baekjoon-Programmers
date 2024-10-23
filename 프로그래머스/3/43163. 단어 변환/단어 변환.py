from collections import deque
def TrueorFalse(now,next,words):
    count = 0
    for i in range(len(now)):
        if now[i] == next[i]:
            count += 1
    if count == len(now) - 1:
        return True
    else:
        return False
                
def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append(begin)
    info = {}
    info[begin] = 0
    
    while queue:
        v = queue.popleft()
        for i in words:
            if TrueorFalse(v,i,words) == True and i not in info:
                info[i] = info[v] + 1
                queue.append(i)


    if target in info:
       return info[target]
    else:
       return 0
