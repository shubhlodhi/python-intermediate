# employee_1 = {"Name" : "Shubh" , "Profession" : "Computer Scientist"}
# employee_2 = {"Name" :"ethen" , "Profession": "Software Engineer"}
# employee_3 = {"Name" :"Mathew" , "Profession": "Android Development"}

# colllection = [employee_1,employee_2,employee_3]
# for i in colllection:
#     print(i)

#  make an empty dict and add employee:
employees_data = []
for i in range(0,30):
    new_employee = {"1" : "Shubh" , "Profession" : "Computer Scientist"}
    employees_data.append(new_employee)

    # print(employees_data)
# first we create a list then append the dict in this list through list
for i in employees_data[:5]:
    print(i)

print(f"how many employess are created {len(employees_data)}")

# here we change the value of first five employee :
for i in employees_data[:5]:
    if i["Profession"] == "Computer Scientist":
        i["1"] = "Mathew"
        i["Profession"] = "Software Engineer"
for i in employees_data[:5]:
    print(f"the new employee are {i}")
# employees_data = employees_data.append(i)
# change the values of dict:
    if i["Profession"] == "Software Engineer":
        i["1"] = "Erin"
        i["Profession"] = "Doctor"
for i in employees_data[:5]:
        print(i)

# a list in a dictinary:

food = {"1" : ["Pasta" , "Trffl"] ,
        "2" :["Chai" , "Sutta"]
        ,"3" : ["Sikanji" , "Sutta"]
        }
# print(food["1"])
print(f"You ordered 1 number ")
# for i in food["2"]:
for i in food.values():
     print(f"order are {i}")
