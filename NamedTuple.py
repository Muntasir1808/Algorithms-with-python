from collections import namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
cyan = Color(red=55, blue=155, green=255)
print(cyan.blue)
black = Color(red=0, green=0, blue=0)
print(black.blue)


# to see some more example on this topic see hackerrank namedtuple challenge example

