def countDiv(number):
    count = 0
    for i in range(1, int(number ** (0.5) + 1)):
        if i * i == number:
            count += 1
            continue
        if number % i == 0: 
            count += 2
        
    return count
            
def solution(number, limit, power):
    answer = 0
    arr =  []
    for i in range(1,number + 1):
        value = countDiv(i)
        if value > limit:
            value = power
        arr.append(value)
    
    return sum(arr)