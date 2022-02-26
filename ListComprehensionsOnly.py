# list = [1, 2, "a", 3.24]
# small notes about list comprehensions
# 1. [exp for val in collections]
# 2. [exp for val in collections if <condition>]
# 3. [exp for val in collections if <condition> and <condition2>]
# 4. [exp for val in collections 1 and val in collections 2]

# square of items in lists...using normal method
# square = []
# for items in range(1, 11):
#     square.append(items ** 2)
# print(square)

# using list comprehensions the following code could be written in this way
# square = [items ** 2 for items in range(1, 11)]
# print(square)

# lets say we have a list of names and we want to print the names that starts with the letter 'M'
# movies = ["Muntasir", "Monowar", "Sejan", "Buri", "Habib", "Moon", "Kahar"]
# my_names = [names for names in movies if names.startswith('M')]
# print(my_names)

# lets say we have a list of movies containing both title of the movie and the year it was released and what if we
# want to get the list of the movies which are released before the year 2000
# movies = [("Citizen Kane", 1947), ("Hacksaw Ridge", 2015), ("Star Wars", 1999), ("The old man", 2013)]
# prev = [title for (title, year) in movies if year < 2000]
# print(prev)

# suppose we have a vector and we want to perform the scaler multiplication of the vector and what if we want multiply
# the elements in the vector by 4
# v = [2, -3, 1]
# my_new_vec = [item * 4 for item in v]
# print(my_new_vec)

# lets use list comprehension to compute cartesian product
# if A = {1, 2} and B = {x, y}
# the cartesian product A X B = {(1,x), (1,y), (2,x), (2,y)}
A = [1, 3, 5]
B = [2, 4, 6]
my_product = [(a, b) for a in A for b in B]
print(my_product)

