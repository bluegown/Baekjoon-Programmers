
def solution(clothes):
    answer = 0
    info = {}
    for i in range(len(clothes)):
        info[clothes[i][1]] = 0
    
    for i in range(len(clothes)):
        info[clothes[i][1]] += 1
    
    num = 1
    for key,value in info.items():
        num = num * (value + 1)

    return num - 1