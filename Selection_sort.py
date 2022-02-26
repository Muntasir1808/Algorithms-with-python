a = list(map(int, input().split()))
for items in range(0, len(a)):
    minimum = items
    for j in range(items+1, len(a)):
        if a[j] < a[minimum]:
            minimum = j
    a[items], a[minimum] = a[minimum], a[items]
print(*a)
