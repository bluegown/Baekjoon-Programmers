def solution(progresses, speeds):
    answer = []
    # 7, 3 ,9 니까 
    # 7 
    # 앞에가 7일이 걸리는데, 내가 지금 3일이 걸리네 ! -> 뒤에꺼도 7로 통일됨
    # 위는 maxValue > day인 경우
    # 처리불가. continue
    # 앞에가 7일이 걸리는데, 뒤에는 9일이 걸려 ! -> 이제 처리할 수 있겠다ㅏㅏ
    # 위는 maxValue < day인 경우. 
    # 이때 append(count)
    
    maxValue = (100 - progresses[0]) // speeds[0]
    if (100 - progresses[0]) % speeds[0] != 0:
        maxValue += 1
    count = 1
    # maxValue < day면 처리 가능함 count += 1
    for i in range(1,len(progresses)):
        day = (100 - progresses[i]) // speeds[i] # 각 소요되는 날짜에 대한 배열
        if (100 - progresses[i]) % speeds[i] != 0:
            day += 1
        if maxValue < day: # 10 > 1이니까 처리 가능함
            answer.append(count)
            maxValue = day
            count = 1
        else: # 10 
            count += 1

        
        
            
            
    if count != 0:
        answer.append(count)
            
        
        
    return answer