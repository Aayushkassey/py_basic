from abc import ABC, abstractmethod

class Vehicle(ABC):
    vehicle_count = 0

    def __init__(self, brand, model, speed=0):
        self._brand = brand
        self._model = model
        self.__speed = speed
        Vehicle.vehicle_count += 1

    @abstractmethod
    def drive(self):
        pass

    def set_speed(self, speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed

    def show_details(self):
        print(f"{self._brand} {self._model}, Speed: {self.__speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, speed=0):
        super().__init__(brand, model, speed)
        self.fuel_type = fuel_type
    
    def drive(self):
        print(f"Car {self._brand} {self._model} is driving smoothly on the road.")

    def show_details(self):
        print(f"{self._brand} {self._model}, Speed: {self.get_speed()} km/h, Fuel: {self.fuel_type}")

class Bike(Vehicle):
    def __init__(self, brand, model, has_gear, speed=0):
        super().__init__(brand, model, speed)
        self.has_gear = has_gear

    def drive(self):
        print(f"Bike {self._brand} {self._model} is zooming through traffic.")

    def show_details(self):
        gear_text = "with gears" if self.has_gear else "no gears"
        print(f"{self._brand} {self._model}, Speed: {self.get_speed()} km/h, {gear_text}")

    

class Bus(Vehicle):
    def __init__(self, brand, model, capacity, speed=0):
        super().__init__(brand, model, speed)
        self.capacity= capacity

    def drive(self):
        print(f"Bus {self._brand}{self._model}is carrying 40 passengers.")
        

    def show_details(self):
        pass_text= "with passenger" if self.capacity else "no passenger"
        print(f"{self._brand} {self._model}, {pass_text}")


            


car1 = Car("Tesla", "Model 3", "Electric")
bike1 = Bike("Yamaha", "FZ", True)
bus1 = Bus("Volvo", "9700", 40)
# --- Test Abstract Base Class behavior --
print("\n=== Testing Abstract Base Class ===")
print("Is Vehicle abstract?", hasattr(Vehicle, 
'__abstractmethods__'))
# --- Test Inheritance and Polymorphism --
print("\n=== Testing Polymorphism (drive methods) ===")
vehicles = [car1, bike1, bus1]
for v in vehicles:
    v.drive()  # each should print different message
# --- Test Encapsulation (private attribute access) 
print("\n=== Testing Encapsulation (speed setter/getter) ===")
car1.set_speed(120)
bike1.set_speed(80)
bus1.set_speed(60)
print(car1.get_speed())  # Expected 120
print(bike1.get_speed()) # Expected 80
print(bus1.get_speed())  # Expected 60
# Direct access should fail (if encapsulation is correct)
print("\nTrying to access private attribute directly:")
try:
    print(car1.__speed)
except AttributeError:
    print("Access denied: private attribute is encapsulated properly")
# --- Test show_details method override --
print("\n=== Testing show_details() ===")
for v in vehicles:
    v.show_details()  # each should include its specific attributes
# --- Test class vs instance variable --
print("\n=== Testing class variable (vehicle_count) ===")
print("Vehicle count:", Vehicle.vehicle_count)
# Check that instance doesn’t override class variable accidentally
car1.vehicle_count = 99
print("Vehicle.vehicle_count =", 
Vehicle.vehicle_count)
print("car1.vehicle_count =", car1.vehicle_count, 
"(should not affect class variable)")
# --- Test inheritance chain --
print("\n=== Testing inheritance relationships ===")
print(isinstance(car1, Vehicle))  # True
print(isinstance(bike1, Vehicle)) # True
print(isinstance(bus1, Vehicle))  # True
print(issubclass(Car, Vehicle))   # True
print(issubclass(Bike, Vehicle))  # True
print(issubclass(Bus, Vehicle))   # True
print("\nAll tests executed.")