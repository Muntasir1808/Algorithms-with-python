queries = int(input())
for _ in range(0, queries):
    size_and_k = input().split()
    size = int(size_and_k[0])
    k = int(size_and_k[1])
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    b.reverse()
    flag = 0
    for item in range(0, size):
        if a[item] + b[item] < k:
            flag = 1
    if flag == 1:
        print("NO")
    else:
        print("YES")

