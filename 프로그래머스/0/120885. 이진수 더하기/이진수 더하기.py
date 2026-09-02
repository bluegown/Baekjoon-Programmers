def change_2(num):
    ans = []
    if num == 0:
        return '0'
    while num >= 1:
        ans += str((num % 2))
        num = num // 2
    return ''.join(ans[::-1])
    
def change(arr):
    num = 1
    sumValue = 0
    for i in arr[::-1]:
        sumValue += num * int(i)
        num = num * 2
    return sumValue

def solution(bin1, bin2):
    answer = ''
    sumValue = change(bin1) + change(bin2)
    
    answer = change_2(sumValue)
    
    
    return answer