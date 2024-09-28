import sys
def binary_search(elem):
    start = 0
    end = len(LIS) - 1
    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == elem:
            return mid
        elif LIS[mid] > elem:
            end = mid - 1
        else:
            start = mid + 1
    return start


N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
LIS = [arr[0]]

for i in range(N):
    if arr[i] > LIS[-1]:
        LIS.append(arr[i])
    else:
        index = binary_search(arr[i])
        LIS[index] = arr[i] # 값의 변경

print(len(LIS))