from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((-numbers[0] , 0))
    queue.append((numbers[0] , 0)) #value , index
    while queue:
        value , index = queue.popleft()
        
        index += 1
        if index < len(numbers):
            queue.append((value + numbers[index] , index ))
            queue.append((value -numbers[index] , index))  
        else:
            if value == target:
                answer += 1
    return answer
