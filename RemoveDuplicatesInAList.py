numbers = []
print("Enter 5 numbers:")
for item in range(5):
    num = int(input())
    numbers.append(num)
print(numbers)
unique = []
for item in numbers:
    if item not in unique:
        unique.append(item)
print(unique)