a = list(map(int, input().split()))
flag = False
for items in range(0, len(a)):
    for j in range(0, len(a) - 1 - items):
        if a[j] > a[j+1]:
            flag = True
            a[j], a[j+1] = a[j+1], a[j]
    if not flag:
        print(flag)
        break
print(*a)
