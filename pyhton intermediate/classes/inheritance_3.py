# when we add the child class and use the parent class in the child class
class car:
    def __init__(self , name , year , company):
        self.company = company
        self.year = year
        self.name = name
        self.odo_meter = 0
        self.tank = "12L"
    def way_of_show(self):
        return f"{self.company} {self.name} {self.year}"
    def odometer(self):
        return f"the car was drived {self.odo_meter}:KM"
    # def update_odometer(self , mileage):
    #     self.odo_meter = mileage
    #     return f"the update value of odometer is {self.odo_meter}:KM"

    def update_odometer(self , mileage):
        if self.odo_meter <= mileage:
            self.odo_meter = mileage
        else:
            print("you roll back")

# these both function above update_ododneter is define a updation of odometer it checks the value of odo_meter if value odo is larger hen miles then it 
# remians the same value it print else statement.
    def increment_odoemeter(self , miles):
        self.odo_meter += miles

    def Tank(self):
     print(f"this car have a {self.tank}")

class Battery():
    def __init__(self , battery_size=300):
        self.battery_size = battery_size 

    def describe_battery(self):
        return f"the size of this car battery is {self.battery_size} KW"
    def range(self, range):
        if self.battery_size == 50:
            return range
        elif self.battery_size == 100:
            return range

        print(f"the car goes to {range} miles")
    # def range(self):
    #     if self.battery_size == 40:
    #         range  = 200
    #     elif self.battery_size == 80:
    #         range  = 450
        

    #     print(f"the car goes to {range} miles")

class Electric_car(car):
    def __init__(self, name, year, company):
        super().__init__(name, year, company)
        self.KWH = 20
        self.battery = Battery()
    def kwh(self):
        return f"the car kilo watt is {self.KWH}"
    # def get_range(self):
    #     if self.range == 150:
    #         range = 
        
        
    
    def Tank(self):
        print("this car dosn't have a gas tank")

cars = car("Gallardo" , 2020 , "Lamborghini")
electric = Electric_car("GT-5" , 2023 , "Nissan")

print(electric.way_of_show())
print(electric.kwh())
print(electric.Tank())
print(cars.Tank())
print(electric.battery.describe_battery())
print(electric.battery.range(56))
