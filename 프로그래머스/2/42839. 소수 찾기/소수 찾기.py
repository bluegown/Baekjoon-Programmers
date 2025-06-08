from itertools import permutations
def is_prime(x,primelist):
    if x < 2:
        return False
    if x in primelist:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    arr = []
    primelist = []
    for i in range(1,len(numbers) + 1):
        perList = list(set(map(''.join,permutations(numbers,i))))
        for i in perList:
            if is_prime(int(i),primelist) == True:
                primelist.append(int(i))
                answer += 1
                
    return answer