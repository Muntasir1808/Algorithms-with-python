def recursive_coin_change(amount, note_list):
    minimum_changes_req = 0
    i = 0
    length = len(note_list)
    while amount > 0 and i < length:
        if note_list[i] <= amount:
            t_val = amount // note_list[i]
            print(f"{note_list[i]} cents {t_val} times")
            minimum_changes_req += t_val
            amount = amount - t_val * note_list[i]
        i += 1
    return minimum_changes_req


notes = [9, 6, 1]
change = int(input())
res = recursive_coin_change(change, notes)
print(f"total {res} changes requires")

