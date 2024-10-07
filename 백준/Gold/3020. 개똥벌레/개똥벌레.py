import sys




N,H = map(int,sys.stdin.readline().split())
down = [0] * (H+1)
up = [0] * (H+1)
for i in range(N):
      height = int(input())
      if i % 2 == 0:
          down[height] += 1
      else:
          up[height] += 1
# 석순과 종유석을 구분해서 입력받는다

for i in range(H-1,0,-1):
    down[i] += down[i+1]
    up[i] += up[i+1]



minValue = N
count = 0
for i in range(1,H+1):
   
   if minValue > down[i] + up[H-i+1]:
      minValue = down[i] + up[H-i+1]
      count = 1
   elif minValue == down[i] + up[H-i+1]:
      count +=1
    
print(minValue,count)
           
      

       

