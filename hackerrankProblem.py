n = int(input())
a = list(map(int, input().split()))
a.sort()
minimum = float("inf")
for item in range(0, len(a)):
    if item + 1 < len(a) and minimum > abs(a[item] - a[item+1]):
        minimum = abs(a[item] - a[item+1])
print(minimum)






