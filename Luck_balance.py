# def luck_balance(luck_with_possibilities, max_lose):
#     list_having_importance = []
#     list_having_no_importance = []
#     for items in range(0, len(luck_with_possibilities)):
#         if luck_with_possibilities[items][1] == 1:
#             list_having_importance.append(luck_with_possibilities[items])
#         else:
#             list_having_no_importance.append(luck_with_possibilities[items])
#     list_having_importance.sort(key=lambda x: x[0], reverse=True)
#     # print(list_having_importance)
#     luck_increase = list_having_importance[0:max_lose]
#     luck_decrease = list_having_importance[max_lose:]
#     # print(luck_increase)
#     # print(luck_decrease)
#     luck_increase_sum = 0
#     luck_decrease_sum = 0
#     no_importance_sum = 0
#     for items in range(0, len(luck_increase)):
#         luck_increase_sum += luck_increase[items][0]
#     for items in range(0, len(luck_decrease)):
#         luck_decrease_sum += luck_decrease[items][0]
#     for items in range(0, len(list_having_no_importance)):
#         no_importance_sum += list_having_no_importance[items][0]
#     result = luck_increase_sum + no_importance_sum - luck_decrease_sum
#     return result
#
#
# nk = input().split()
# n = int(nk[0])
# k = int(nk[1])
# contests = []
# for _ in range(n):
#     contests.append(list(map(int, input().split())))
# print(contests)
# print(luck_balance(contests, k))

# This was my first solution
# and after learning new things my solution is

def luck_balance(contests, max_lose):
    important = []
    not_important = []
    for val, specific in contests:
        if specific == 1:
            important.append(val)
        else:
            not_important.append(val)
    # print(contests)
    # print(important)
    # print(not_important)
    important.sort(reverse=True)
    luck_increase = sum(important[0:max_lose]) + sum(not_important)
    luck_decrease = sum(important) - sum(important[0:max_lose])
    res = luck_increase - luck_decrease
    return res


nk = input().split()
n = int(nk[0])
k = int(nk[1])
luck_with_possibilities = []
for _ in range(n):
    luck_with_possibilities.append(list(map(int, input().split())))
# print(luck_with_possibilities)
print(luck_balance(luck_with_possibilities, k))
