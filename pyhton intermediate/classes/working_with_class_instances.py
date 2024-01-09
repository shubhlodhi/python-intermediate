class car:
    def __init__(self , name , year , company):
        self.company = company
        self.year = year
        self.name = name
        self.odo_meter = 0
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
        # return self.odo_meter # if we pass this statement then it trace the value of update_ododmeter function value.
# these function is increment the value of upadte odo_meter value

bmw = car("A6" , 2023 , "Audi")
print(bmw.way_of_show())
print(bmw.odometer())
bmw.odo_meter = 11
print(bmw.odometer())
(bmw.update_odometer(90))

print(bmw.odometer())
print(bmw.increment_odoemeter(100))
print(bmw.odometer())
# change the value of audometer in a coditon
# print(bmw.increment_odometer(12))




