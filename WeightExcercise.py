weight = int(input("Enter weight: "))
unit = input("(l)bs Or (K)g: ")
up = unit.upper()
if up == 'K':
    calc = weight * 2.20
    print(f"You are {calc} pounds")
else:
    calc = weight * 0.45
    print(f"You are {calc} kilograms")
