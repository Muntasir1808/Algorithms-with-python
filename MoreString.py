course = 'Python for beginners'
print(course)
print(course.upper())
print(course.lower())

# find character which will return index
print(course.find('t'))
# replace
print(course.replace('beginners','absolute beginners'))

# existence of character or word in a string which returns boolean
print('Python' in course)
# find length of a string
print(len(course))

# title method makes the first character of each word in capital
s = 'I go to school'
print(s.title())
