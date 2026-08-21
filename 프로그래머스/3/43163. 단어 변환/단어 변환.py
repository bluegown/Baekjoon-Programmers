from collections import deque
def compare(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count > 2:
            return False
    if count == 1:
        return True
    else:
        return False
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0 # 반환할 수 없는 경우
    visited = dict()
    for i in words:
        visited[i] = 1
    visited[begin] = 1
    queue = deque()
    queue.append((begin, 0))
    
    
    while queue:
        v, count = queue.popleft()
        if v == target:
            break
        visited[v] = 0
        count += 1
        for i in words:
            if visited[i] == 1 and compare(v, i) == True:
                queue.append((i, count))
                
        
        
    return count