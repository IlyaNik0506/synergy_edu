class Car(object):
    # brand = 'mazda'
    # max_speed = 100
    # color = 'black'
    def __init__(self, brand, max_speed, color):
        self.brand = brand
        self.max_speed = max_speed
        self.color = color

    def upgrade(self):
        self.max_speed += 25


class Truck(Car):
    def __init__(self, brand, max_speed, color, trailer, tonnage):
        super().__init__(brand, max_speed, color)
        self.tonnage = tonnage
        self.trailer = trailer


# car = Car('mazda', 100, 'black')
# print(car.brand, car.max_speed, car.color)
# truck = Truck('Volvo', 120, 'black', 1000, 2)
# print(truck.brand, truck.max_speed, truck.color, truck.tonnage, truck.trailer)

