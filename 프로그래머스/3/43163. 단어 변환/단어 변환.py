from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    queue = deque()
    queue.append((begin, 0))
    while queue:
        element, answer = queue.popleft()
        if element == target:
            return answer
        for i in range(len(words)):
            count = 0
            for j in range(len(words[0])):
                if element[j] == words[i][j]:
                    count += 1
            if count == len(words[0]) - 1:
                queue.append((words[i],answer + 1))
            
    return answer