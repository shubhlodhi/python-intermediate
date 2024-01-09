# make a restaurant class in this two function: 1. oprn restauarnt function and describe restaurant
# with three different instances
# create user class and define the user , and greeting the user and describe_user an print the summary of each user.


class restaurant:
    def __init__(self , name , type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        return f"{self.name } is {self.type}"

    def open_status(self):
        return f"{self.name} Hotel are open 24X7"


Hen = restaurant("COD" , "NON-VEG")
print(Hen.describe_restaurant())
print(Hen.open_status())




class user:
    def __init__(self , name , E_mail , Username):
        self.name = name
        self.E_mail = E_mail
        self.Username = Username
        self.company = "GOOGLE" 
    
    def describe_user(self):
        return f"Name:{self.name}\n E-mail:{self.E_mail}\n Username:{self.Username}\n Organization:{self.company}"
    
    def greeting(self):
        return f"Congratulation you are Hired as a developer {self.name}"
    
    def summary_comp(self):
        return f"{self.company}'s Member is very glad that you are the part of our organization"

user1 = user("shubh" ,"shubh.singh9411@gmail.com" , "Sslrp")
print(user1.describe_user())
print(user1.greeting())
print(user1.summary_comp())
