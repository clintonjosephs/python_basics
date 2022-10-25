class Car:
    brand = ''
    model = ''
    year =  0
    speed = 0
    mileage = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class ElectricCar(Car):
    battery_size = 0
    battery_type = ''

    def __init__(self, brand: str, model: str, year: int):
        super().__init__(brand, model, year)

class HybridCar(Car):
    battery_size = 0
    battery_type = ''
    fuel_tank = 0


car = Car()
car.year = 2020

electric_car = ElectricCar()
electric_car.year = 2020
electric_car.battery_size = 100

hybrid_car = HybridCar()
hybrid_car.year = 2020
hybrid_car.battery_size = 100