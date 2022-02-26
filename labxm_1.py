n = int(input())
a = list(map(int, input().split()))
minimum = 0
low = 0
high = n - 1
while low < high:
    mid = (low+high) // 2
    if a[mid - 1] > a[mid] > a[mid + 1]:
        minimum = a[mid]
        break
    elif a[mid+1] < a[mid]:
        minimum = a[mid+1]
        break
    elif a[mid] < a[high]:
        high = mid
    else:
        low = mid
print(minimum)
