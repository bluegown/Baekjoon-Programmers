from math import factorial
def solution(n, k):
    numbers = list(i for i in range(1,n+1))
    answer = []
    k -= 1 # 앞에 수 고정하고 나머지 돌려돌려
    
    while numbers:
        index , k  = divmod(k , factorial(len(numbers) - 1))
        answer.append(numbers.pop(index))
    return answer