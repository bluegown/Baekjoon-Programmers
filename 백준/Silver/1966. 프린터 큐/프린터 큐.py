import sys
from collections import deque
T = int(input())

for _ in range(T): 
     N,M = map(int,sys.stdin.readline().split())
     
     arr = list(map(int,sys.stdin.readline().split()))
     queue = deque()
     for i in range(len(arr)):
         queue.append((i,arr[i]))
     count = 0
     if len(queue) == 1:
          print(1)
     else:
       while True:
          if queue[0][1] == max(queue,key = lambda x:x[1])[1]: 
            # max(queue,key = lambda x:x[1]) -> x[1]을 기준으로 한 max값 tuple 반환
            # 그래서 , 거기에서 [1]을 해줘야 완전한 value가 뽑힘
            count += 1 # 만약 현재값이 맥스값이라면 카운트 +1만큼 (프린트를 한 것이므로) 
            if queue[0][0] == M: # 만약 내가 찾던 원소라면
               print(count)
               break 
            else:# 프린트는 했는데, 내가 찾던 원소는 아니야 ...
               queue.popleft() # 그럼 그냥 내쫒아야지
          else: #그냥 뒤로 보내버려
             queue.append(queue.popleft())
             

               

          
          