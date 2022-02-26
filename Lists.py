numbers = [10, 20, 30, 40, 50, 60]
friends = ['Habib', 'Tanvir', 'Sejan', 'Sajid']
print(friends)
# to extend another list with the current one
friends.extend(numbers)
print(friends)
# to insert an element in the list
friends.insert(2, "Buri")
print(friends)
# to remove an element from the list
friends.remove('Sajid')
print(friends)
# to clear the whole list
numbers.clear()
print(numbers)
# we can also count particular element in the list
# let's add another habib in the list and count
friends.insert(2, 'Habib')
print(friends.count('Habib'))

# other important things on list is on the folder operationsOnTheList .....
