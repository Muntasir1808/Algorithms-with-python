# lambda function is the function which are defined without the name
# var = lambda arguments: expression

# def add(x, y):          this can be written as
#     return x + y        var = lambda x, y : x + y
# lambda function can be used in some built in function which is the best use

# map function without using lambda function
# find sq of each element of a list
def square(x):
    return x * x


a = [1, 2, 3, 4]
y = list(map(square, a))
print(y)
#
# # similar thing but different approach by using lambda
# var = map(lambda x: x * x, a)
# print(list(var))

# adding two list using map function where both the list should be of same length and both list
# should contain either string or integer but not both at the same time
# a = [1, 2, 3, 4]
# b = [1, 1, 1, 1]
# v = map(lambda x, z: x + z, a, b)
# print(list(v))
#
# x = lambda a, b, c: a + b + c
# print(x(5, 6, 2))


# lambda within user defined function
# def A(x):
#     return lambda w: x + w
#
#
# t = A(4)
# print(t(10))

# filter function filters the elements of the iterable based on some functions
# filter function is used to filter the unwanted elements
# syntax: filter(function, iterables)
# to get the even numbers form 1 to 10 we can do like
# for items in range(1, 11):
#     if items % 2 == 0:
#         print(items)

# similar thing can be done using filter writing just one line of code
even = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(even)

# reduce function reduces some iterables into a single element using some function
# to perform some computations on list or tuples which output will be single element then reduce is used
# syntax: reduce(function, iterables)
# to use reduce we need to import it
import functools

num = [1, 2, 3, 4]
# to perform sum operation
r = functools.reduce(lambda x, y: x + y, num)
print(r)


