# alien_0  = {"eyes" : "blue" , "points" : 1}
# print(alien_0["eyes" ])
# print(alien_0["points"])
# new_points = alien_0["points"]
# print(new_points)

# # # adding new value pairs:
# alien_0["planet"] = "tittanium"

# print(alien_0)
# print(alien_0["planet"])
# # adding value in blank dictonary:
# alien_1 = {}
# alien_1["name"] = "MegaMind"
# alien_1["planet"] = "Blue Planet"
# alien_2 ={}
# alien_2["name"] = "Mathew"
# alien_2["planet"] = alien_1["planet"]
# print(alien_1)
# print(alien_2)
# print(alien_1["name"])
# # changing the value of dictinonary:
# alien_1["planet"] = "gignatic"
# new_planet = alien_1["planet"]
# print(f"{alien_1['name'] } New Planet is now {new_planet.title()}")
# # let find this concept with an example:
alien_2 = {"Present_position": 2, "Speed": "medium"}
P_postion = 0
print(f"present location {alien_2['Present_position']}")
if alien_2["Speed"] == "medium":
   P_postion = 4
elif alien_2["Speed"] == "slow":
   P_postion = 5
else:
   print("Hard to find location")

alien_2["Present_position"] = P_postion + alien_2["Present_position"]
print(f"New loaction will be now {alien_2['Present_position']}")

# # removing key-value pairs:
del alien_2["Present_position"]
print(alien_2)
# #  dictionary have similar objects:
programmer = {"shubh" : "Python",
              "lodhi": "Python",
              "gandu": "C"}
gandus = programmer["gandu"]
print(f"assholes favirate language is {gandus}")


# use get functions:
programming = programmer.get("lodi" , "there is no langauge for this user") # here this print the value of any key if key is not matched to the get value argument then it print the 
# followinh line: "there is no langauge for this user , here lodi is not available in upper dictinary that;s why it is printed this statement.
print(programming)

user_0 = {"Username": "Shubh Lodhi",
          "password":"Hello",
          "confirm":"hello,",
          "Shubh":"Added"
          }
user_online  = ["Shubh" ]
erin = "Erin"
for user in user_0.keys():
   # online_user = ("shubh" , "lodhi") 
   print(f"congratulation you join the channel {user.title()}")
   if  user   in  user_online:

      # user_1 = user_0[user].title()
      print("Please join the channel " , user)
      print(f"{user.title() } it's your faviorate langauages")
   elif user:
      print(f"you are already  joined {(user_0.keys())}")
  
   if erin not in user_0.keys():
      print(f"please join the channel {erin.title()}" )

# # use every key in a soretd manner:


#    if user in (user_0.keys()):
#       print(user_0)
# for user in sorted(user_0.keys()):

   print(f"chances of every participants in this manner:{user.title()}")
# # print all values of dict:
# for i in (user_0.values()):
#    print(f"form critirea are {user.title()}")

# #  use dict in set:
# user_3 = {
#    "shubh": "python",
#    "demorgan": "Python",
#    "ashutosh":"C"
# }
# for use in set(user_3.values()):
#    print(f"languages are {use.title()}")

# diction = {
#    "shubh" :["Python" , "Django"],
#    "lodhi": ["Python" , "Flask"],

# }  
# for i , y in diction.items():
#    print(f"hello {i}")
#    for i in y:
#       print(f"you languages are {i}")