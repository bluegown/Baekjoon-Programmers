import sys
def binary_search(elem,b):
    global count
    start = 0
    end = M-1

    while start <= end:
        mid = (start + end) // 2
        if b[mid] >= elem:
            end = mid - 1
        elif b[mid] < elem:
            start = mid + 1
    count += start

    
T = int(input())

for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))
    b = list(map(int,sys.stdin.readline().split()))
    a.sort()
    b.sort()
    count = 0
    for i in a:
        binary_search(i,b)
    print(count)

