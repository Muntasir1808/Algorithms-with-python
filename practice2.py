a = list(map(int, input().split()))
res = []
# while True:
#     for items in range(1, len(a)):
#         if a[items] > a[items - 1]:
#             res.append(a[items-1])
# print(len(a))
for items in range(1, len(a)):
    if a[items] > a[items - 1]:
        res.append(a[items-1])
print(res)
