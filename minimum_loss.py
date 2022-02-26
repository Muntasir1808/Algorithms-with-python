y = int(input())
a = list(map(int, input().split()))
b = []
for item in range(0, len(a)-1):
    for j in range(item, len(a)):
        b.append(a[item]-a[j])
b.sort()
for item in range(0, len(b)):
    if b[item] > 0:
        print(b[item])
        break
