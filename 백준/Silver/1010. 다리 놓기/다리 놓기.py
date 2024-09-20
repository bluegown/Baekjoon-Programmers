import sys
import itertools
T = int(input())
for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    div = N
    num = M
    value = 1
    divValue = 1
    for i in range(1,N+1):
        value = value * num
        num = num - 1
    for j in range(1,N+1):
        divValue = divValue * div
        div -= 1
    value = value // divValue
    print(value)

    # 29 * 28 ... / 13 * 12 ... 1