from collections import deque
# 주어지는 숫자의 개수는 2~ 20
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((-numbers[0],0))
    queue.append((numbers[0],0)) 
    # queue의 첫번째 원소는 숫자, 두번째 원소는 인덱스
    
    while queue:
        value, index = queue.popleft()
        index += 1
        if index < len(numbers):
            queue.append((value + numbers[index], index))
            queue.append((value - numbers[index], index)) 
        if value == target and index == len(numbers):
            answer += 1

            
    return answer