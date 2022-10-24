class Car():
    """A simple attempt to represent a car."""
    color = 'red'
    model = 'BMW'
    speed = 0
    brand = ''
    fuel_tank = 0
    number_of_wheels = 0
    engine_size = 0
    mileage = 0

    def __init__(self, color, model, speed, brand, fuel_tank, number_of_wheels, engine_size, mileage):
        """Initialize attributes to describe a car."""
        self.brand = brand
        self.fuel_tank = fuel_tank
        self.number_of_wheels = number_of_wheels
        self.engine_size = engine_size
        self.mileage = mileage
        self.color = color
        self.model = model
        self.speed = speed

    def current_speed(self):
        """Show the current speed of the car."""
        print(f"The current speed of the car is {self.speed} km/h")


car_one = Car('red', 'BMW', 12, 'BMW', 100, 4, 2.0, 0)
car_one.current_speed()


