try:
    age = int(input("Age: "))
    print(age)
    income = 20000
    risk = income / age
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Can not divide by zero")