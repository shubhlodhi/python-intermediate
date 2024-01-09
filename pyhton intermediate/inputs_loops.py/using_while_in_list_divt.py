# to collect the infromation from list or store the information  we use while loop in dict and list :
# because using while the list and dict allows you to collect and store the info:


#  moving a one list from another list:
#  to transfer the unverified user list to verified user list :
unnconfirm_user = ["shubh" , "lodhi" , "kindy"]
confrimed_user = []
while unnconfirm_user:   # here while track the list of unconfirmed user:
    current_user = unnconfirm_user.pop()


    print(f"verify user are {current_user.title()}")
    confrimed_user.append(current_user) # here we append the unconfrimed user into the confirmed user:


for i in confrimed_user:
    print(f"confirmed user are in the new list" , i)
    print(i.title())

#  removing all instances from list using while loops:
# we remove multiple same value from the list using while loops:

bad_habits = ["Smoking" , "Gym" , "Meditiation" , "Negative_thinking" , "Negative_thinking"] 
# (bad_habits.remove("Negative_thinking")) # here it removes only one value:
# print(bad_habits)


while "Negative_thinking" in bad_habits:
    bad_habits.remove("Negative_thinking")
print(bad_habits)


#  filing a dictionary with input user:
# here we take user  name and his response:
 
polling = {}
active_flag  = True
while active_flag:
    name = input("tell your name")
    response = input("what is your faviorate music")
#  store the rsponse in a dictionary:
    polling[name] = response

#  check it is take poll or not:
    poling = input("would take poll to another person 'Yes/No'")
    if poling == "No":
        active_flag = False
 
for i  , j in polling.items(): # it track both values and keys in dict
    print(f"{i.title()} favrate music is {j.title()}")
    
# print(polling)

    