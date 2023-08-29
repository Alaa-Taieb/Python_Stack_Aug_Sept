class Car:
    # Class Attribute
    cars = []
    # Constructor
    # Self is a reference to the object being created.
    def __init__(self, model, color):
        # model and color are instance attributes
        self.model = model
        self.color = color
        self.__mileage = 0
        Car.cars.append(self)

    # An instance method
    def car_details(self):
        return f"This is a {self.color} {self.model}"

    def drive(self, miles):
        self.__mileage += miles
        return self

    def drive_safely(self, miles):
        if miles > 20:
            self.__mileage += 20
        else:
            self.__mileage += miles
        return self

    def display_mileage(self):
        print(f"This car was driven for {self.__mileage} miles.")
        return self

    # Classmethod
    @classmethod
    def how_many_cars(cls):
        return len(cls.cars)

    @staticmethod
    def is_valid_model(model):
        valid_models = ["Tesla Model S", "Toyota Corolla", "Ford Mustang"]
        return model in valid_models




class ElectricCar(Car):
    def __init__(self, model, color, battery_size):
        # Using 'super()' to call the parent class's __init__ method (Constructor)
        super().__init__(model , color)
        self.battery_size = battery_size

    def car_details(self):
        base_details = super().car_details()
        return f"{base_details}, It has a {self.battery_size}Khw Battery."
# class Math:

#     @staticmethod
#     def calculate_rect_area(width, height):
#         return width * height
    
#     @staticmethod
#     def calculate_square_area(side):
#         return side * side

# Create instances of a class 'Car'
if (Car.is_valid_model("Tesla Model S")):
    my_car = ElectricCar("Tesla Model S", "White", 120)
print(Car.how_many_cars())
my_second_car = ElectricCar("Tesla Model S", "Black", 100)
print(Car.how_many_cars())






# Calling instance methods
print(my_car.car_details())
print(my_second_car.car_details())

# Method chaining
my_car.drive_safely(50).display_mileage().drive_safely(15).display_mileage()
