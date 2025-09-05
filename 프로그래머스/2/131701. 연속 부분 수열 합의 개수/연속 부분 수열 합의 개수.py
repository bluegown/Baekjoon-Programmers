def solution(elements):
    answer = 0
    x = set()
    # 지금 길이가 1이면 초기에 sumValue = 7이잖아
    # 그럼 이제 sumValue = sumValue + 9(elmeents[2]- 7elements[1]
    
    #길이가 2면 초기엔 7 + 9 = 16
    # sumValue = sumValue + 1(arr[3]) - 7arr[1] = 10  # 이떄 
    # sumValue = sumValue + arr[4] - arr[2]
    # sumValue = sumValue + arr[0(5)] - arr[3]
    #sumValue = sumValue + arr[1] - arr[4]
    # sumValue = sumValue + arr[2] - arr[0] # 한바퀴 회전 끝
    # 둘의 인덱스 차이는 길이인 long이 맞음
    length = len(elements)
    for long in range(len(elements)): # 길이
        sumValue = sum(elements[0 : long + 1]) # 0부터 i까지 초기에 더해줌
        x.add(sumValue)
        for index in range(1,len(elements)): # 시작점 지정 (0은 이미 더해줬다)
            sumValue = sumValue + elements[(index + long) % length] - elements[index]
            x.add(sumValue)
    x.add(sum(elements))
            
            
    return len(x)