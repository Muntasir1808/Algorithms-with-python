class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Moved")

    def draw(self):
        print("Draw")


point1 = Point(10, 20)
print(point1.y)

