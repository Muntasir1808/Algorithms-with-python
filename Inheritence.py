class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barking")


class Cat(Animal):
    pass


dog = Dog("Dog")
dog.walk()
dog.bark()
cat = Cat("Cat")
cat.walk()