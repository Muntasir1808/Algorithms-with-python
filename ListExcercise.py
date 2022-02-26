numbers = [10, 20, 30, 40, 50, 90]
maximum = numbers[0]
for item in numbers:
    if item > maximum:
        maximum = item
print(f"Maximum element in the list is {maximum}")