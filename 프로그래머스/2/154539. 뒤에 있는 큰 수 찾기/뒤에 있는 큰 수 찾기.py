def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    # 0,2 / 1,3  / 2,3 / 3,5
    # 0,9 / 1,1 / 2,5 / 3,3 / 4,6 / 5,2 
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            # 스택의 최상단에 있는 
            answer[stack.pop()] = numbers[i]
        stack.append(i)
        
            
        
        
    return answer