def coin_change(change, coins_list):
    n = len(coins_list)
    table = [[x for x in range(change + 1)] for x in range(n)]

    for items in range(0, n):
        for j in range(0, change+1):
            if j == 0:
                table[items][j] = 0
            elif coins_list[items] > j:
                table[items][j] = table[items - 1][j]
            else:
                table[items][j] = min(table[items-1][j], 1+table[items][j-coins_list[items]])
    for items in range(0, len(table)):
        print(table[items])

    summation = 0
    count = 0
    for items in range(n-1, 0, -1):
        if table[n-1][change] == table[n-2][change]:
            count += 1
            print(f"inside {table[n-1][change]} {table[n-2][change]}")
            continue
        # print(f"s = {coins_list[n - 1]}")
        # summation += change - coins_list[n - 1]
        # change = change - coins_list[n - 1]
        print(f"{table[n-1][change]} == {table[n-2][change]}")

    print(summation)
    return table[n-1][change]


coins = list(map(int, input().split()))
change_amount = int(input())
print(coin_change(change_amount, coins))
