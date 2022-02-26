phonebook = {}
n = int(input())

for i in range(n):
    name = input("").lower()
    phoneNumber: str = input("")
    phonebook.update({name: phoneNumber})

while True:
    search = input("")
    output = ""
    if phonebook.get(search) is None:
      print("Not found")
    else:
      output += search + "=" + phonebook.get(search, "")
      print(output)

