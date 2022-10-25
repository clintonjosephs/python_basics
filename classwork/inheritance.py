class Car:
    brand = ''
    model = ''
    year =  0
    speed = 0
    mileage = 0

class ElectricCar(Car):
    battery_size = 0
    battery_type = ''

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