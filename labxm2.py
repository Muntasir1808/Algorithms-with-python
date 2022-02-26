def minimum_jumps(target_meter, jump_length_list):
    n = len(jump_length_list)
    table = [[x for x in range(target_meter + 1)] for x in range(n)]
    for items in range(0, n):
        for j in range(0, target_meter + 1):
            if j == 0:
                table[items][j] = 0
            elif jump_length_list[items] > j:
                table[items][j] = table[items - 1][j]
            else:
                table[items][j] = min(table[items-1][j], 1 + table[items][j - jump_length_list[items]])
    for items in range(0, len(table)):
        print(table[items])

    return table[n-1][target_meter]


jump_list = list(map(int, input().split()))
target = int(input())
print(minimum_jumps(target, jump_list))
