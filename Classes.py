class Point:
    def move(self):
        print("Moved")

    def draw(self):
        print("Drawn")


point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
point2.x = 1
print(point2.x)
point1.move()