from itertools import permutations
def solution(k, dungeons):
    answer = -1
    arr = [i for i in range(len(dungeons))]
    
    turn = list(permutations(arr,len(dungeons)))
    for i in turn: # [0,1,2] , [0,2,1]이 각각의 i다 
        count = 0
        value = k
        for index in i: #index는 그안에 있는 원소들. dungeons[index][0], dungeons[index][1]로 표현
            if dungeons[index][0] > value: # 내가 가지고있는 체력이 더 작은경우
                continue
            if k <= 0:
                break
            else:
                count += 1
                value -= dungeons[index][1]
        answer = max(count, answer)
                
                
        
    return answer