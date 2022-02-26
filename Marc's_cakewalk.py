def jim_burger(orders_and_prep_time, customers):
    timings = []
    for items in range(0, len(orders_and_prep_time)):
        timings.append(sum(orders_and_prep_time[items]))
    # print(timings)
    customers_list = []
    for items in range(customers):
        customers_list.append(items+1)
    # print(customers_list)
    combined_list = []
    inner = []
    for items in range(0, len(timings)):
        inner = timings[items], customers_list[items]
        combined_list.append(inner)
    # print(combined_list)
    combined_list.sort(key=lambda x: x[0])
    # print(combined_list)
    customers_ascending_order = []
    for items in range(0, len(combined_list)):
        customers_ascending_order.append(combined_list[items][1])
    return customers_ascending_order


n = int(input())
o_and_p_time = []
for _ in range(n):
    o_and_p_time.append(list(map(int, input().split())))
res = jim_burger(o_and_p_time, n)
print(*res)
