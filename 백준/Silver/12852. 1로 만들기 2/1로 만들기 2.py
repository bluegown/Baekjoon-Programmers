import sys

N = int(input())

d = [0] * (N+1)
ans = []

for i in range(2,N+1):
    d[i] = d[i-1] + 1
    if i%2 == 0:
        d[i] = min(d[i],d[i//2] + 1)
    if i%3 == 0:
        d[i] = min(d[i],d[i//3] + 1)

print(d[N])
ans.append(N)
count = d[N]
index = N
for i in range(N,0,-1):
    if (i*2 == index or i*3 == index or i+1 == index) and d[i] == count - 1:
        index = i
        count -= 1
        ans.append(i)
    
for i in ans:
    print(i,end= ' ')

