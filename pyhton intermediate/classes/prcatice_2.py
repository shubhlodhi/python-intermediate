# make a restaurant class in this two function: 1. oprn restauarnt function and describe restaurant
# with three different instances
# create user class and define the user , and greeting the user and describe_user an print the summary of each user.


class restaurant:
    def __init__(self , name , type):
        self.name = name
        self.type = type
        self.number_served = 0
    def describe_restaurant(self):
        return f"{self.name } is {self.type}"

    def open_status(self):
        return f"{self.name} Hotel are open 24X7"
    def served(self):
        return f"there are {self.number_served } customer available"
    def number_serverd(self  , served):
        self.number_served = served
        return f"{self.number_served} customer are avalaible"
    def increment_served(self , cust):
        self.number_served += cust


    


Hen = restaurant("COD" , "NON-VEG")
print(Hen.describe_restaurant())
print(Hen.open_status())
print(Hen.number_serverd(5))
print(Hen.increment_served(20))
print(Hen.served())




class user:
    def __init__(self , name , E_mail , Username):
        self.name = name
        self.E_mail = E_mail
        self.Username = Username
        self.company = "GOOGLE" 
        self.login = 1
    
    def describe_user(self):
        return f"Name:{self.name}\n E-mail:{self.E_mail}\n Username:{self.Username}\n Organization:{self.company}"
    
    def greeting(self):
        return f"Congratulation you are Hired as a developer {self.name}"
    
    def summary_comp(self):
        return f"{self.company}'s Member is very glad that you are the part of our organization"
    def logins(self):
        return f"there are {self.login} user is active"
    def inc_login(self , inc):
        self.login += inc
    def ino_login(self , ino):
        self.login -= ino

user1 = user("shubh" ,"shubh.singh9411@gmail.com" , "Sslrp")
print(user1.describe_user())
print(user1.greeting())
print(user1.summary_comp())
print(user1.logins())
(user1.inc_login(11))
print(user1.logins())
(user1.ino_login(1))
print(user1.logins())