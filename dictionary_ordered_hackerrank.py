from collections import OrderedDict
buying_items = OrderedDict()
n = int(input())
for item in range(n):
    item_name, space, price = input().rpartition(" ")
    price = int(price)

    if item_name in buying_items:
        buying_items[item_name] += price
    else:
        buying_items[item_name] = price
for k, v in buying_items.items():
    print(k, v)


