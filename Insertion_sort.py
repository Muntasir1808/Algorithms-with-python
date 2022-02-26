a = list(map(int, input().split()))
for item in range(1, len(a)):
    key = a[item]
    j = item - 1
    while j >= 0 and a[j] > key:
        a[j+1] = a[j]
        j = j - 1
    a[j+1] = key
print(*a)
