# retun  values always have to display its output directly , return  value take a avalur from the function send it to the line of functons:
def get_value(username , password):
    shubh = f"{username} , {password}"
    return shubh

lodhi = get_value("shubh" , "12344")
print(lodhi)

#  making an argument optional:
 
def get_values(first_name  , Last_Name , Middle_name=""):  # non empty string in python interprets is true
    if Middle_name: # here it check if middle name is required or not if miidle name is not required then non empty string if condition is fail the it runs else block:

        full_name = f"{first_name }, {Middle_name} , {Last_Name}"
    else:
        full_name = f"{first_name} , {Last_Name}"
    return full_name
    
jo = get_values("Shubh" , "lodhi" , "singh")
print(jo)
jo = get_values("shubh" , "lodhi")
print(jo)

# returning a dictionary:
# function can return any kind of value and argyments including list and dictionary:
def dict(first_name , second_name):
      preson = {"fisrt": first_name , "secind" : second_name}
      return preson

ff = dict("shubh" , "sara")
print(ff.keys())
print(ff)

#  if statement in dictinary:

def build_name(fisrt_name , last_name , age=None):  # it takes none as a false value
    fun = {"fisrt" : fisrt_name , "sec" : last_name}
    if age:
        fun["age"] = age # here fun["age"] is a dict.keys() value
    return fun

dd = build_name("shubh" , "Lodhi" , 12)
print(dd)

# using a function with a while loop:
def fl(first_name , kast_name):
    fal = f"{first_name}   {kast_name}"
    return fal

while True:
    
    f_name = input("tell your first name")
    if f_name == "Q":
        break
    l_name = input("tell your last name")
    
    if l_name == "Q":

        break


    

    tell = fl(f_name,l_name)

    print(tell)
    


def name(caste , last_name , age=None):
 if age == None:
     new_name = f"{caste} , {last_name}"
     return new_name
 else:
      new_name = f"{caste} , {last_name} , {age}"
      return new_name

# full = f"{last_name} is important for identification of {caste} accroding to the age "
# print(full)



    


