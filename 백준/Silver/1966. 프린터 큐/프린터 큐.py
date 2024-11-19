import sys
from sys import stdin
from collections import deque

testcount = int(input())

x = []
printindex = 0

for i in range(testcount):
    N ,M = map(int,input().split())
    index = M
    array = list(map(int,input().split()))
    queue = deque()
    count = 0
    for element in array:
     queue.append(element)

    
    while len(queue)!=0:
        
        maxelem = max(queue)
        elem = queue.popleft()
        if elem >= maxelem:
            x.append(elem)
            count +=1
            if index == 0:
               print(count)
               break
            index -=1
            if index < 0:
               index = len(queue)-1
            
        else:
            queue.append(elem)
            index -=1
            if index < 0:
               index = len(queue)-1
            


