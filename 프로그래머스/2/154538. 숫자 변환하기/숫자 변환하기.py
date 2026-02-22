def solution(x, y, n):
    answer = 0
    d = [(y + 1)] * (y + 1)
    
    d[x] = 1
    num = x
    for num in range(x,y + 1):
        if num * 3 <= y:
            d[num * 3] = min(d[num * 3], d[num] + 1)
        if num * 2 <= y:
            d[num * 2] = min(d[num * 2], d[num] + 1)
        if num + n <= y:
            d[num + n] = min(d[num + n], d[num] + 1)
            
    if d[y] == y + 1:
        return -1

    return d[y] - 1