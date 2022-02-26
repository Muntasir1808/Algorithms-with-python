a = list(map(int, input().split()))
max_sum = float('-inf')
for item in range(0, len(a)):
    for j in range(item, len(a)):
        summation = 0
        for k in range(item, j+1):
            summation = summation + a[k]

        if summation > max_sum:
            max_sum = summation

print(max_sum)
