def solution(n):
    answer = 0
    # while n > 10:
    #     answer += (n % 10)
    #     n = n // 10
    # answer += n
    # return answer
    for i in str(n):
        answer += int(i)
    return answer
        