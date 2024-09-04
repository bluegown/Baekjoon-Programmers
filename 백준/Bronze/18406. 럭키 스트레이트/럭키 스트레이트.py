import sys

def sum(num):
    sum = 0
    for i in num:
        sum = sum + int(i)

    return sum
N = list(input())

arr1 = N[0:len(N)//2]
arr2 = N[len(N)//2:len(N)]
if sum(arr1) == sum(arr2):
    print("LUCKY")
else:
    print("READY")

