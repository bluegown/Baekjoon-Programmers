def radixChange(num, radix): # num은 대상 숫자, radix는 진법
    
    if num == 0:
        return '0'
    nums = []
    while num:
        num, digit = num // radix , num % radix
        nums.append(str(digit))
    
    return ''.join(reversed(nums)) 
        
def solution(n):
    answer = 0
    return int(radixChange(n,3)[::-1],3) # 역순 뒤집고 3진법 -> 자동 10진법 변환