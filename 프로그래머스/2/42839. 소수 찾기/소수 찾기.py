from itertools import permutations
def is_prime (num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    p = set()
    for i in range(1,len(numbers) + 1):
        prime = list(set(permutations(numbers, i)))
        print(prime)
        for num in prime:
            prime_number = int(''.join(num[:]))
            if is_prime(prime_number):
                if prime_number not in p:
                    p.add(prime_number)  
                    answer += 1
                     
    return answer