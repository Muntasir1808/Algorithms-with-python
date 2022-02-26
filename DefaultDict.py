from collections import defaultdict
food_list = "Habib"
food_count = defaultdict(int)  # default value of int is 0
for food in food_list:
    food_count[food] += 1  # increment element's value by 1

# print(food_count)
for k, v in food_count.items():
    print(k, ":", v)

# to learn about defaultdict the following link is useful enough
#  https://www.accelebrate.com/blog/using-defaultdict-python
