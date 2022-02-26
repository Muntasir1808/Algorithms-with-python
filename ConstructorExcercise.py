class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} is talking")


person = Person("Muntasir")
person.talk()

person2 = Person("John Smith")
person2.talk()