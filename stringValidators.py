# check for the hackerrank problems in python named "string validators"
string = input()
for item in range(len(string)):
    if string[item].isalnum():
        print("True")
        break
    if item == len(string) - 1:
        print("False")

for item in range(len(string)):
    if string[item].isalpha():
        print("True")
        break
    if item == len(string) - 1:
        print("False")

for item in range(len(string)):
    if string[item].isdigit():
        print("True")
        break
    if item == len(string) - 1:
        print("False")

for item in range(len(string)):
    if string[item].islower():
        print("True")
        break
    if item == len(string) - 1:
        print("False")

for item in range(len(string)):
    if string[item].isupper():
        print("True")
        break
    if item == len(string) - 1:
        print("False")