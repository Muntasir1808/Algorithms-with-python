def knapsack(capacity, combined_list, index, length):
    if capacity <= 0 or index == length:
        return 0
    elif capacity < combined_list[index][1]:
        fraction = capacity/combined_list[index][1]
        return fraction * combined_list[index][0] + knapsack(0, combined_list, index+1, length)
    else:
        return combined_list[index][0] + knapsack(capacity - combined_list[index][1], combined_list, index + 1, length)


v = list(map(int, input().split()))
w = list(map(int, input().split()))
c = int(input())
n = len(v)
values_by_items = []
for items in range(0, len(w)):
    values_by_items.append(v[items] / w[items])
I = []
inner = []
for items in range(0, len(w)):
    inner = [v[items], w[items], values_by_items[items]]
    I.append(inner)
print(I)
I.sort(key=lambda x: x[2], reverse=True)
print(I)
i = 0
res = knapsack(c, I, i, n)
print(res)
