from collections import Counter
my_list = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
print(Counter(my_list))
# we can see specific items counter using tuple
print(Counter(my_list).items())
# to see the keys
print(Counter(my_list).keys())
print(Counter(my_list).values())
