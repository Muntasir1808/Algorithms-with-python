import utils

numbers = [12, 46, 11, 56, 2, 8]
result = utils.find_max(numbers)
print(result)

# another way to do this thing
from utils import find_max
result2 = find_max(numbers)
print(f"Coming form another way of import {result2}")