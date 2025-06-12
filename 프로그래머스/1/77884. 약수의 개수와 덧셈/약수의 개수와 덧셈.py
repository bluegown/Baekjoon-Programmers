def countPrime(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 2
            if i == num // i:
                count -= 1 # 10 * 10과같은 중복되는 경우
    if count % 2 == 0:
        return num
    else:
        return -num

def solution(left, right):
    answer = 0
    for element in range(left, right + 1):
        answer += countPrime(element)
    return answer