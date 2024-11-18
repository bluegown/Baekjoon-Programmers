import sys

T = int(input())

for _ in range(T):
    arr = list(input())
    x = []
    stop = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            x.append('(')
        else:
            if len(x) == 0:
                stop = 1
                break
            x.pop()

    if stop == 1 or len(x)!=0:
        print("NO")
    elif len(x) == 0:
        print("YES")
    
   



    


