#  passing a list in function
def greet(username):
    for i in username: # here we generate a for loop for accesing the arguments of funtion:
        shubh = f" Hello {i}"
        print(shubh)
    
user = ["shubh" , "Maga" , 23]
print(greet(user))

# modying  a list in a functions:

