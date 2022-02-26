a = list(map(int, input().split()))

# stock span
# l = len(a)
# res = [1]
# span = 1
# for i in range(1, len(a)):
#     j = i - 1
#     if a[i] >= a[j]:
#         while a[i] >= a[j] and j >= 0:
#             span += 1
#             j -= 1
#         res.append(span)
#         span = 1
#     else:
#         res.append(1)
# print(res)

# stock span using stack
l = len(a)
stack = []
res = []
stock_span = []
for item in range(len(a)):
    while stack and stack[-1][0] <= a[item]:
        stack.pop()
    if not stack:
        stack.append([a[item], item])
        res.append(-1)
    if stack and stack[-1][0] > a[item]:
        res.append(stack[-1][1])
        stack.append([a[item], item])
print(res)
# nearest greater element on the left
# l = len(a)
# result = []
# stack = []
# for items in range(len(a)):
#     while stack and stack[-1] <= a[items]:
#         stack.pop()
#     if stack and stack[-1] >= a[items]:
#         result.append(stack[-1])
#         stack.append(a[items])
#     elif not stack:
#         result.append(-1)
#         stack.append(a[items])
# print(result)






# nearest greater element on the right
# l = len(a)
# res = [-1] * l
# for i in range(len(a)):
#     # next_ele = -1
#     for j in range(i+1, len(a)):
#         if a[j] > a[i]:
#             # next_ele = a[j]
#             res[i] = a[j]
#             break
#
# print(res)

# stack = []
# answers = []
# for items in range(len(a) - 1, -1, -1):
#     while stack and stack[-1] <= a[items]:
#         stack.pop()
#     if stack and stack[-1] > a[items]:
#         answers.append(stack[-1])
#         stack.append(a[items])
#     elif not stack:
#         answers.append(-1)
#         stack.append(a[items])
# answers.reverse()
# print(answers)
