# example = set()
# # another way to declare set
# # whenever we need to compare the values of the lists set can be used
# # to create a set from a list
# example2 = set([2, 3, 4, 5])
# print(example2)

# # to assign a set directly
# example3 = {1, 2}

# # for sets order does not matter ....duplicates are not stored inside of the set
# # while printing each time the results will not be the same
# # different types of data can be stored in the set
# example.add(43)
# example.add(False)
# example.add(23.33)
# example.add("Thorium")
# print(example)

# # to find the length of the set
# print(len(example))

# # to remove an element from the set
# example.remove(43)
# print(example)

# # if we try to remove an element which is not in the set then it will give an error
# # to avoid this error discard method is used
# example.discard(23.33)
# print(example)
# example.discard(100)
# print(example)

# # to add multiple elements in the set use update method
# example.update([6, 7, 8, 9])
# print(example)

# # we can also add another set in the set
# s2 = set("Habib")
# example.update(s2)
# print(example)

# set union and intersection
odds = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}
prime = {2, 3, 5, 7}
# perform set union
print(odds.union(even))
# perform intersection
print(odds.intersection(prime))

# # testing if one particular element in the set
# print(2 in prime)
# print(6 in odds)
# print(9 not in even)

# # difference method in set
# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# # to see the value of s1 which are not in s2
# s3 = s1.difference(s2)
# print(s3)

# # to see the values which are not common between the sets or unmatched values between the sets
# s4 = s1.symmetric_difference(s2)
# s5 = s2.symmetric_difference(s1)
# # here both the results will be the same
# print(s4)
# print(s5)

# # some practical example of using set can be for removing duplicate elements from the list
# li = [1, 1, 3, 2, 3, 6, 5]
# print(set(li))
# # or to print it as a list also
# l2 = list(set(li))
# print(l2)

# # another example
employees = ['Habib', 'Sejan', 'Buri', 'Muntasir', 'Moon', 'Chandu', 'Tittu']
gym_membership = ['Habib', 'Buri', 'Muntasir']
developers = ['Sejan', 'Moon', 'Chandu', 'Muntasir']
# first of all find the names which has both gym membership as well as developers
all_rounder = set(gym_membership).intersection(developers)
print(all_rounder)
# names which are neither gym members or developers
res = set(employees).difference(gym_membership, developers)
print(res)
