import re
# match function in regex used to test the input string with the specified pattern or not it checks the beginning of
# the input if matches then
# on success it returns matched object and on failure it returns None
line = "Python and Java it gives Jython"
r1 = re.match(r'Java', line)
print(r1)
# r2 = re.match(r'Python', line)
# print(r2)
# line2 = "pet:cat I love cats"
# match = re.match(r'pet:\w\w\w', line2)
# print(match)
# # to see the matched objects
# print(match.group(0))

# search function will search the whole string instead of just the beginning but will allow only the first occurrence
# line3 = "I love pet:cow"
# res = re.search(r'pet:\w\w\w', line3)
# print(res)
# print(res.group(0))

# to get all the occurrences we have to use findall function
# line4 = "pet:cat I love pet:cow"
# var = re.findall(r'pet:\w\w\w', line4)
# print(var)

# split is used for splitting on which basis
# line5 = "pet:cat I love cows pet:cow cow is useful"
# r = re.split(r'pet:\w\w\w', line5)
# print(r)

# replace function can be used to replace one or more words of a string
# str1 = "john@abc.com and alice@pqr.com"
# res = re.sub(r'@\w+', "xyz", str1)
# print(res)
