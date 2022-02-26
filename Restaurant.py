class Restaurant:
    def __init__(self, res_name, cuisine_type):
        self.res_name = res_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant " + str(self.res_name).title() +
              " Cuisine type is " + str(self.cuisine_type).title())

    @staticmethod
    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, val):
        self.number_served = val

    def increment_number_served(self, increase):
        self.number_served += increase
        print("Served people- " + str(self.number_served))


class IceCreamStand(Restaurant):
    def __init__(self, res_name, cuisine_type):
        super().__init__(res_name, cuisine_type)
        self.flavors = ["vanilla", "strawberry", "chocolate"]

    def show_flavors(self):
        print("Available flavors: " + str(self.flavors).title())


r1 = Restaurant("KFC", "Fast-food")
r1.describe_restaurant()
print(r1.number_served)
r1.set_number_served(20)
print(r1.number_served)
r1.increment_number_served(4)
r1.increment_number_served(5)

# inheritance
ice = IceCreamStand("Polar", "cream")
ice.show_flavors()