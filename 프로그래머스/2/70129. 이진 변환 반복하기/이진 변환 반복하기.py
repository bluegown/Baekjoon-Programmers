def radixtoChange(num,radix):
    if num == 0:
        return '0'
    
    nums = []
    while num:
        num, digit = divmod(num,radix)
        nums.append(str(digit))
    
    return ''.join(reversed(nums))

def solution(s):
    answer = []
    count = 0
    exection = 0
    deleted = 0
    while s != '1':
        exection += 1 
        count = 0
        for i in s:
            if i == '1':
                count += 1
        deleted += len(s) - count
        s = radixtoChange(count,2)
    return [exection,deleted]