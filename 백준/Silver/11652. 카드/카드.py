import sys

answer = 0
N = int(input())
d = dict()

for _ in range(N):
    i = int(input())
    d[i] = d.get(i,0) + 1

result = sorted(d.items(), key = lambda x: (-x[1],x[0]))

print(result[0][0])



    

