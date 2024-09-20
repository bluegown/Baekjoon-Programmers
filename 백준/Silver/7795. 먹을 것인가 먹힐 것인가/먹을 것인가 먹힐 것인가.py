import sys


    
T = int(input())

for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))
    b = list(map(int,sys.stdin.readline().split()))
    a.sort()
    b.sort()
    count = 0
    for i in a:
        for j in b:
            if i > j:
                count += 1
    print(count)

