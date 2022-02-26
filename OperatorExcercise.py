name = input("Enter your name: ")
name_length = len(name)
if name_length < 3:
    print("Name must be at least 3 characters")
elif name_length > 50:
    print("Name must be less than 50 characters")
else:
    print("Name is okay")