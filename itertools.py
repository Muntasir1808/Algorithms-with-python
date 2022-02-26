from itertools import product
print(list(product([1, 2, 3], repeat=3)))
print(list(product([1, 2, 3], [3, 4])))
A = [[1, 2, 3], [3, 4]]
print(tuple(product(*A)))
print(product(*A))

# see hackerrank example in itertools product in website
