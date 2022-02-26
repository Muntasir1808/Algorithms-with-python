a = list(map(int, input().split()))
max_sum = float('-inf')
for item in range(0, len(a)):
    summation = 0
    for j in range(item, len(a)):
        summation += a[j]
        if summation > max_sum:
            max_sum = summation
print(max_sum)
