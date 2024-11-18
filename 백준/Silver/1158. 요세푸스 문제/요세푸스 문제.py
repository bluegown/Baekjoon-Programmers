import sys

N,K = map(int,sys.stdin.readline().split())

arr = [(i+1) for i in range(N)]

ans = []
index = 0

for i in range(N):
    index += (K-1)
    if index >= len(arr):
        index = index % len(arr)
    ans.append(str(arr[index]))
    arr.pop(index)

    


print("<",", ".join(ans)[:],">", sep='')



    
    