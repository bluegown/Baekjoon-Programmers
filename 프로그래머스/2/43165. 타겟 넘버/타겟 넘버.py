from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((-numbers[0] , 0))
    queue.append((numbers[0] , 0))
    sumValue = 0
    while queue:
        value , index = queue.popleft()
        index += 1
        if index < len(numbers):
            queue.append((-numbers[index] + value, index))
            queue.append((numbers[index] + value , index))
        if value == target and index == len(numbers):
            answer += 1
        
        
        
    
    return answer