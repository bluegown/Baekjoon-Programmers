def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(x**(0.5)) + 1):
        if x % i == 0:
            return False
    
    return True # True가 소수
from itertools import permutations
def solution(numbers):
    answer = 0
    
    arr = []
    for i in range(1,len(numbers) + 1):
        arr.append(list(set(map(''.join,permutations(numbers, i)))))


    temp = set()
    for i in arr:
        for j in i:
            temp.add(int("".join(j)))
    print(temp)
    
    for i in list(temp):
        if is_prime(i) == True:
            answer += 1
            
        

    return answer