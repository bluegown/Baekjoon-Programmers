import sys

A = int(input())
T = int(input()) # count가 얘랑 같아지는 순간
x = int(input()) # 0이면 뻔 1이면 데기 

arr = []
count = 0
index = 0
bun = degi = 1
while True:
    prev_number = bun
    index += 1
    for _ in range(2):
        arr.append((bun,0))
        bun += 1
        arr.append((degi,1))
        degi += 1
    for _ in range(index+1):
        arr.append(((bun,0)))
        bun += 1
    for _ in range(index+1):
        arr.append((degi,1))
        degi += 1
    if prev_number < T <= bun:
        print(arr.index((T,x)) % A)
        break

