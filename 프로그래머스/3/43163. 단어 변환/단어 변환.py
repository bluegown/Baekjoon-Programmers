from collections import deque
def find_next(begin, target):
    cnt = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            cnt += 1 # 한번까지 다름 허용
        if cnt >= 2:
            return False
    return True
def solution(begin, target, words):
    answer = 0
    queue = deque()
    count = 0
    if target not in words:
        return 0
    queue.append((begin, 0))
    while queue:
        v , count = queue.popleft()
        for word in words:
            if find_next(v, word):
                if v == target:
                    return count
                queue.append((word, count + 1))
            
    return count   
        