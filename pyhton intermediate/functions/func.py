def greet(user):
    return("hello" , user)

print(greet("lodhi"))

def hell():
    return("Congratulations you are now in a real world")

print(hell())

#  positional arguments:
def describe_elements(username , pet_name):
    print(f"your name is {username}")

    print(f"your pet name is {pet_name}")

hello = describe_elements("shubh" , "Lucy")
print(hello)

# multiple functions call:

SS = describe_elements("Lodhi" , "Dollar")
GG = describe_elements("varun" , "Tiger")
print(SS , GG)

#  Order Matter in positional Arguments:

dd = describe_elements("JOJO" , "Shubh" )
print(dd)

# Key Words Arguments:

describe_elements(pet_name="JOJO" , username="Koski")
# a key-word Arguments is a name value that you pass to the function. there is no worry about correctly ordering your arguments

# Default Values:
def describe_value( Name_dog ,Pet_Type = "Dog" ):
    print(f"Hi ,{Pet_Type.title()}")
    print(f"my {Pet_Type} name is {Name_dog} ")

DD = describe_value("Kusion")

#     Equivalent Functions calls: we call one funtions in many ways.

describe_elements( "jojo" , "Lodhi" )
describe_elements(pet_name=  "JOJO" , username="shubh")
describe_elements("shubh" , pet_name="jojo")

