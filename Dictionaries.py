customer = {
    "name": "John smith",
    "age": 30,
    "is_verified": True
}
# the value in the dictionaries can be anything ...it can be even list
print(customer["name"])
# it can also display values using get
print(customer.get("age"))
# we can also update info outside
customer["name"] = "Jack Smith"
print(customer["name"])
# we can easily add new key value outside the dictionaries
customer["birthday"] = "Jan 10 1990"
print(customer["birthday"])
# we can print the the values of the key using get method
print(customer.get("name"))
# if the key is absent in the dictionary then it will return "none" which means absence of value
print(customer.get("email"))
# we can set values of the key which was not in the dictionaries like we can set value for email
print(customer.get("email", "jack@gmail.com"))

# we can see all the keys in the dictionaries as well as values
print(customer.keys())
print(customer.values())

# we can also sort keys and values of the dictionaries
print(sorted(customer.items()))
print(sorted(customer.keys()))

# in this example an error is occurred because to sort values all the data types should be same
# print(sorted(customer.values()))

# to remove particular key values from dictionaries
del customer["name"]
print(customer.items())

# to remove all entries use clear method
# customer.clear()
# print(customer)

# iterate over keys
for item in customer.keys():
    print(item)

# iterate over values
for item in customer.values():
    print(item)
# to iterate over both key and values
for k, v in customer.items():
    print(k, "is from", v)
# in dictionary we can store bunch of key and value pairs...keys should be unique
