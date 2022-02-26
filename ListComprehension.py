numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = []
# for item in numbers:
#     my_list.append(item)
# print(my_list)

# we can do the whole thing in just writing one line of code which is list comprehensions
# my_list = [item for item in numbers]
# print(my_list)

# if we want the square items present in the list
# my_list = [item * item for item in numbers]
# print(my_list)

# we want the even numbers from the given list
# my_list = [item for item in numbers if item % 2 == 0]
# print(my_list)

# I want a letter number pair for each letter abcd and each number 0123
# without list comprehension the following code would be
# for letter in 'abcd':
#     for number in range(4):
#         my_list.append(letter, number)
#         print(my_list)

# using list comprehension the following code will be
my_list = [(letter, number) for letter in 'abcd' for number in range(4)]
print(my_list)

# dictionary comprehensions using zip function
# names = ['Bruce', 'Clark', 'Peter', 'Logan']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine']
# dict_zip = dict(zip(names, heros))
# print(dict_zip)

# the upper code could be done by using dictionary also
# names = ['Bruce', 'Clark', 'Peter', 'Logan']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine']
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

# by writing dictionary comprehensions like lists comprehensions we can writer in this way
# names = ['Bruce', 'Clark', 'Peter', 'Logan']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine']
# my_list = {name : hero for name, hero in zip(names, heros)}
# print(my_list)

# we can also print the list without any specific key and values ..here for bruce : batman
# names = ['Bruce', 'Clark', 'Peter', 'Logan']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine']
# my_list = {name : hero for name, hero in zip(names, heros) if name != 'Bruce'}
# print(my_list)

# set comprehensions
# nums = [1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 9]
# my_set = set()
# for item in nums:
#     my_set.add(item)
# print(my_set)

# this whole thing could be done in just one line of code using set comprehensions
# nums = [1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 9]
# my_set = {n for n in nums}
# print(my_set)
