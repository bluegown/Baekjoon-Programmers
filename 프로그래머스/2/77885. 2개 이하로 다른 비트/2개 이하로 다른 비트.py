
def solution(numbers):
    answer = []
    for elements in numbers:
        if elements % 2 == 0:
            answer.append(elements + 1) # 짝수인 경우 무조건 다음 수가 정답
        else:
            y = elements + 1
            answer.append(y + ((elements ^ y) >> 2))
            
    return answer