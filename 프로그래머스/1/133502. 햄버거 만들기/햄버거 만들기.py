from collections import deque
def solution(ingredient):
    answer = 0
    queue = []
    for i in range(0,len(ingredient)):
        index = i
        queue.append(ingredient[i])
        if len(queue) >= 4:
            if queue[-4 : ] == [1,2,3,1]:
                answer += 1
                queue.pop()
                queue.pop()
                queue.pop()
                queue.pop()

    return answer