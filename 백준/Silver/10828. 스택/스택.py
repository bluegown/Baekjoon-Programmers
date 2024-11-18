
import sys
from sys import stdin
N = int(input())
stack = []
stacksize = 0
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.append(command[1])
        stacksize+=1
    elif command[0] == "pop":  
        if stacksize!= 0:
            print(stack.pop())
            stacksize -=1
        else:
            print(-1)
    elif command[0] == "size": 
        print(stacksize)

    elif command[0] == "empty":
        if stacksize == 0:
            print(1)
        else:
            print(0)   
    elif command[0] == "top": 
        if stacksize!= 0:
            print(stack[-1]) 
        else:
            print(-1)        
    