def change_to_digit(n):
    st = ""
    while n > 0:
        st += str(n % 2)
        n = n // 2

    return ''.join(st)
def solution(s):
    answer = []
    count = 0
    removedZero = 0
    print(s.count("0"))
    while s!= "1":
        length = len(s) - s.count("0") # 0 제거후 길이
        removedZero += s.count("0")
        s = change_to_digit(length)
        count += 1
        
        
        
        
    return [count, removedZero]