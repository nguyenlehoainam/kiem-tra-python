class Vehicle:
    def __init__(self, make):
        self.make = make
    
    def description(self):
        return f"Vehicle Make: {self.make}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model
    
    def description(self):
        return f'''Car Make: {self.make}
 Model: {self.model}'''

class electriccar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
    
    def description(self):
        return f'''Electric Car Make: {self.make}
 Model: {self.model} 
 Battery Size: {self.battery_size} '''


vehicle = Vehicle("Audi")
car = Car("lamborghini", "lamborghini urus")
electric_car = electriccar("Tesla", "tesla v9", 100)

print(vehicle.description())
print(car.description())
print(electric_car.description())
