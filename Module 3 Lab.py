# Name: Rachel Smiley
# File Name: Module 3 Lab.py
# Description:
#    This program defines a Vehicle superclass and an Automobile subclass.
#    It prompts the user to enter details about a car, stores the information,
#    and then displays the vehicle data in a clear, readable format.
# Variables:
#    vehicle_type (str): Type of vehicle (e.g., car, truck, etc.)
#    year (str): Year the automobile was manufactured
#    make (str): Manufacturer of the automobile
#    model (str): Model name of the automobile
#    doors (str): Number of doors (2 or 4)
#    roof (str): Type of roof (solid or sun roof)

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def display_info(self):
        print("\nVehicle Information:")
        print(f"  Vehicle type: {self.vehicle_type}")
        print(f"  Year: {self.year}")
        print(f"  Make: {self.make}")
        print(f"  Model: {self.model}")
        print(f" Number of doors: {self.doors}")
        print(f"  Type of roof: {self.roof}")

def main():
    print("Enter car details:")

    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")

    while True:
        doors = input("Number of doors (2 or 4): ")
        if doors in ["2", "4"]:
            break
        print("Please enter 2 or 4.")
    
    while True:
        roof = input("Type of roof (solid or sun roof): ").lower()
        if roof in ["solid", "sun roof"]:
            break
        print("Please enter 'solid' or 'sun roof'.")
    
    car = Automobile(year, make, model, doors, roof)

    car.display_info()

if __name__ == "__main__":
    main()
