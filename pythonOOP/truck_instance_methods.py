class Truck:
     
    def __init__(self, name, color):
        self.name = name
        self.color = color
     
    def speed(self, speed):
        return "{} speeding at {}".format(self.name, speed)
truck = Truck("Wagon","Red")
print(truck.speed(20))