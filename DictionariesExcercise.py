phone = input("Phone: ")
phone_number_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    # output += phone_number_mapping.get(ch, "!") + " "
    output += phone_number_mapping.get(ch, "!") + " "
print(output)