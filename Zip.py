name = ["Sunny", "Habib", "Buri"]
company = ["Dell", "Apple", "MS"]
zipped = list(zip(name, company))
print(zipped)

# to iterate through zip
for a, b in zipped:
    print(a, b)