from collections import deque
def solution(numbers, target):
    answer = 0
    
    queue = deque()
    queue.append((numbers[0], 0))
    queue.append((-numbers[0], 0))
    
    while queue:
        value, idx = queue.popleft() #숫자 , 몇번째인지 카운트
        idx += 1
        if idx < len(numbers): # 아직 연산이 다 안되었다면?
            queue.append((value + numbers[idx], idx ))
            queue.append((value - numbers[idx], idx ))
        else:
            if value == target:
                answer += 1
    return answer