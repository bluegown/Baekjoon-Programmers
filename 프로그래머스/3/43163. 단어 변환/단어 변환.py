from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    queue = deque()
    queue.append((begin, 0))
    used_words = set()
    used_words.add(begin)
    n = len(begin)
    while queue:
        v, cnt = queue.popleft()
        if v == target:
            return cnt
        for word in words:
            count = 0
            for j in range(n):
                if word[j] == v[j]:
                    count += 1
            if count == n - 1 and word not in used_words:
                queue.append((word, cnt + 1))
            
        
    return 0