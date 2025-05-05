# 15:39 문제 읽기 시작
def solution(line):
    answer = []
    
    crossDot = []
    for i in range(len(line)-1):
        A = int(line[i][0])
        B = int(line[i][1])
        E = int(line[i][2])
        
        for j in range(i+1,len(line)):
            C = int(line[j][0])
            D = int(line[j][1])
            F = int(line[j][2])
            if A*D == B*C: # 분모가 0인 경우는 계산할 필요 없음
                continue
            x = (B*F - E*D) / (A*D - B*C)
            
            y = (E*C - A*F) / (A*D - B*C)
            if int(x) == x and int(y) == y:
                if (x,y) not in set(crossDot):
                    crossDot.append((int(x),int(y)))
    
    crossDot = sorted(crossDot,key = lambda x:x[0])
    xlen = crossDot[-1][0] - crossDot[0][0]
    max_xvalue , min_xvalue = crossDot[-1][0], crossDot[0][0]
    
    crossDot = sorted(crossDot,key = lambda x:x[1])
    ylen = crossDot[-1][1] - crossDot[0][1]
    
    max_yvalue , min_yvalue = crossDot[-1][1], crossDot[0][1]
    
    print(min_xvalue,max_xvalue)
    print(min_yvalue,max_yvalue)
    
    crossDot = sorted(crossDot,key = lambda x:(x[0],x[1]))
    
    for col in range(max_yvalue,min_yvalue-1,-1):
        str = ""
        for row in range(min_xvalue,max_xvalue+1):
            if (row,col) in set(crossDot):
                str += '*'
                print(row,col)
            else:
                str += '.'
        answer.append(str)
 
                
                
            
            
            
        
    return answer