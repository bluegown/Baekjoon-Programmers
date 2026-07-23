def solution(number, k):
    answer = []
    
    for num in number:
        while k > 0 and answer and answer[-1] < num: # 스택 맨 위원소가 number[i]보다 작다면?
            k -= 1
            answer.pop() # 남아있을 자격이 없으니까 쫓아내
        answer.append(num)
    return ''.join(answer[:len(answer) - k ])