a = list(map(int, input().split()))
max_so_far = 0
summation = 0
for item in range(0, len(a)):
    if summation + a[item] > 0:
        summation = summation + a[item]
    else:
        summation = 0
    max_so_far = max(summation, max_so_far)
print(max_so_far)

