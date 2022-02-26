n, k = map(int, input().split())
a = list(map(int, input().split()))
position = [0 for i in range(n+1)]
for element, index in zip(a, range(0, n)):
    position[element] = index

item = 0
while item < n and k > 0:
    if a[item] == n-item:
        item += 1
        continue
    a[position[n-item]] = a[item]
    position[a[item]] = position[n - item]
    a[item] = n - item
    position[n-item] = item

    k -= 1
    item += 1
print(*a)

