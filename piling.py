def piling(stack):
    left_runner = 0
    right_runner = len(stack)-1
    current_cube = float('inf')
    while left_runner <= right_runner:
        left_val = stack[left_runner]
        right_val = stack[right_runner]
        if right_val <= left_val <= current_cube:
            current_cube = left_val
            left_val += 1
        elif left_val <= right_val <= current_cube:
            current_cube = right_val
            right_val -= 1
        else:
            return "No"
    return "Yes"


for _ in range(int(input())):
    n = int(input())
    stack = list(map(int, input().split()))
    res = piling(stack)
    print(res)


# for _ in range(int(input()):
#     n = int(input())
#     stack = list(map(int, input().split()))
#     flag = 0
#     for items in range(len(stack)):
#         while stack:
#             greater = max(stack[0], stack[-1])
#             d = stack.index(greater)
#             popped = stack.pop(d)
#             # print(popped)
#             if stack:
#                 if popped > stack[0] and popped > stack[-1]:
#                 # print(f"inside popped = {popped} stack[0] = {stack[0]} stack[-1] =                     {stack[-1]}")
#                     continue
#                 else:
#                    flag = 1
#                    print("No")
#                    break
# if flag == 0:
#     print("Yes")












