def solution(i, j, k):
    answer = 0
    
    for element in range(i,j+1): # 이래야 i ~ j까지 들어가겠지?
        answer += str(element).count(str(k))
    return answer