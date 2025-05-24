def hanoi(n,start,to,mid,answer):
    if n == 1:
        answer.append([start,to])
        return answer
    hanoi(n - 1, start, mid , to , answer) # 
    answer.append([start,to]) # 3번 탑에 가장 큰놈 옮기기
    hanoi(n - 1, mid, to, start, answer)
    
def solution(n):
    answer = []
    hanoi(n, 1 , 3 , 2 , answer)

    return answer