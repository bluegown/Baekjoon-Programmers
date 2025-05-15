#22:39 읽기 시작
def solution(s):
    answer = 1001
    
    if len(s) == 1:
        return 1
    for slice_value in range(1, (len(s) // 2 + 1)): 
        arr = [] # 파싱한 배열
        num = 0 # 인덱스
        for index in range(len(s)):
            if len(s[num : num + slice_value]) == 0:
                continue
            arr.append(s[num : num + slice_value])
            num += slice_value
        # arr 배열까지는 문제 없음 , 1부터 len(s) // 2 + 1까지 슬라이싱한게 순서대로 

        stack = []
        stack.append(arr[0])
        last_value = arr[0]
        count = 1
        count_arr = ''
        
        for i in range(1,len(arr)):
            stack.append(arr[i]) # arr[i] 원소 스택에 넣고

            if stack[-2] == stack[-1]: # 만약 연속되는 원소라면?
                count += 1 #    
            else: # 마지막 원소랑 다르다? -> 지금까지 연속됐던거 넣어줄 시간이다
                if count > 1: # 연속됐던게 있다면 앞에 숫자도 붙여주고
                    count_arr += str(count)
                count_arr += arr[i-1]# 
                count = 1 # 1로 초기화
                last_value = arr[i]
                
        if count != 1:
            count_arr += str(count)
        count_arr += arr[-1]

        
        answer = min(answer,len(count_arr))
    
            
            
    
    return answer