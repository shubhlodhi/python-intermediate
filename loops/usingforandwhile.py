# reservation application
#  bulk resrvation , age , name , sex.
print(" welcome to ticket bookin website")
travel = input("enter yes if you want to book or no if you dont want to travel")
while travel == "yes":
    h = int(input("enter number of passenger"))
    for h in range(1,h+1):
        name  = input("enter your name")
        age = input("enter your age")
        sex  = input("enter your sex")
        print(name,age,sex)
        cong = print("whoo your ticket is book")
travel = input("Enter if you forget something")        