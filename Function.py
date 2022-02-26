def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome to abroad")


print("Start")
greet_user("John", "Smith")
print("finish")
# keyword arguments where we can refer position for arguments
greet_user(first_name="Smith",last_name="John")
