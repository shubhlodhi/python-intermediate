# creating the class dog:
class dog:
    

    def __init__(self , name , age): 
        self.name = name
        self.age = age

    def write(self):
        return f"my dog name is{self.name}"
    
    def sit(self):
        return f"{self.name} is now sitting"
          
#  here assign the mil variable to the class dog where parameter is name=lucy , age=7
mil = dog("lucy" , 7)
# call the mil variable , now mil is store the property of dog class and we call it whenever we want
# print(mil.name)
# print(mil.age)
#  now mil is defined in the class dog so we use the function sit in the mil class. called as calling method.
# print(mil.sit())

#  creating the multiple instances:
mils = dog("jojo" , 7)
milss = dog("jojo" , 8)
print(f"hello {mils.name} and age is {mils.age}" )
print(mils.sit())
print(f"hello {milss.name} and age is {milss.age}" )
print(milss.sit())
