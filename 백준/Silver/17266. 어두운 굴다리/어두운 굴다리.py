import sys

N = int(input())
M = int(input())



arr = list(map(int,sys.stdin.readline().split()))


res = 0

if M == 1:
    res = max(arr[0],N - arr[0]) # 왼쪽 오른쪽 검토
else:
    for i in range(M):
        if i == 0:
            x = arr[i]
        elif i == M-1:
            x = N - arr[i]
        else:
            distance = arr[i] - arr[i-1]

            if distance % 2 == 0:
                x = distance // 2
            else:
                x = (distance // 2) + 1
        res = max(res,x)


print(res)

    

