numbers = [2, 3, 1, 9, 3, 12, 8]
# to add a number in the list
numbers.append(13)
print(numbers)
# to insert a number at any position on the list
numbers.insert(0, 28)
print(numbers)
# to remove a single element
numbers.remove(2)
print(numbers)
# to remove last element using pop
numbers.pop()
print(numbers)

# to remove all the elements of the list
# numbers.clear()
# print(numbers)

# to check existence of an element in a list which returns the first occurrence of the element
pos = numbers.index(1)
print(pos)

# we can check it in another way using 'in' which returns a boolean value
print(50 in numbers)
# counting occurrences of a number
print(numbers.count(3))
# to sort the list
numbers.sort()
print(numbers)

# sorting in descending order ...to do this after sorting in ascending we have to call reverse
numbers.reverse()
print(numbers)

# copy of one list to another
numbers2 = numbers.copy()
print(numbers2)
