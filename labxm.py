def knapsack_combinations(target_meter, jump_length_list):
    n = len(jump_length_list)
    table = [[0 for x in range(target_meter + 1)] for x in range(n)]
    for items in range(0, n):
        for current_target in range(0, target_meter + 1):
            if current_target == 0:
                table[items][current_target] = 1
            elif jump_length_list[items] > current_target:
                table[items][current_target] = table[items - 1][current_target]
            else:
                table[items][current_target] = table[items - 1][current_target] + table[items][current_target - jump_length_list[items]]
    for items in range(0, len(table)):
        print(table[items])
    return table[n - 1][target_meter]


jump_list = list(map(int, input().split()))
target = int(input())
print(knapsack_combinations(target, jump_list))


