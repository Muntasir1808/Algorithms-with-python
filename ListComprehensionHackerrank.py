n = int(input())
arr = map(int, input().split())
z = sorted(list(arr))
z.reverse()
maxmimum = max(list(z))
print(z)
for item in z:
    if item < maxmimum:
        print(item)
        break
