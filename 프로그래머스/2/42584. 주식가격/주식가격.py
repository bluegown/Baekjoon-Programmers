from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        v = queue.popleft()
        time = 0
        for price in queue:
            if price < v:
                time += 1
                break
            else:
                time += 1
        answer.append(time)
        
    return answer