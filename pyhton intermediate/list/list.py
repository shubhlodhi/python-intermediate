h = ["shubh" , "sneha " , "khushi"]
for woker in h:
    print(f"{woker.title()}  you are great\n")



h = ["shubh" , "sneha " , "khushi"]
for woker in h:
    print(f"{woker.title()}  you are great")
    print(f"{woker.title()} thanks come again\n")
    # print("thanks for part of our organization    \n")

#  after loop
print("thanks for part of our organization")

# print(range(1,5))  waste

# for i in range(0 , 4):
    # print(i)

# n = list(range(0,6))

# even numbers

# n = (range(0,7)) waste
# print(n)
# even = list(range(2 , 11 , 2))  # here last 2 is increment eery value in range function
# print(even)

# sqaures of list
squares = []
for sq in range(1,6):
    squares.append(sq**2)
    # squ = sq**2

    # squares.append(squ)
print(squares)

list = [1,2,3,4,5,6,7]
print(min(list))
print(max(list))
print(sum(list))
# print(list.count()) wrong

# list comphrension

sq = [value**2 for value in range(1,11)]
print(sq)                                                                  
# slicing through list
players = ["shubh" , "marina" , "shasha" , "engineer"]
print(players[0:2])
print(players[:4])
print(players[-4:])
# use for loop
print("players which are selected")
for i in players[0:2]:
    print(i.title())

pl = players[3:]
print("my favirote coder is ")
print(players)

print("our favirote is")
print(pl)

dimensions = (200,40,30)
print(dimensions)
print(dimensions[0])
print(dimensions[1])
print(dimensions[2])

# dimensions[0 ] = 5
# print(dimensions)
dimension = (200,30)
for i in dimension:
    print(i)

dimensionss = (12,300)
for i in dimensionss:
    print(i)
print("previous knowledge")




dimensionss =(300,12)
for i in dimensionss:
    print(i)
print("future knowledge") 

# requested = str(input("enter your choice"))
# if requested != "mushrooms":
    # print(f"your tooping is not available")
# else:
    # print(" your toping is available")

list = ["Bmw"  , "ciaz" , "camaro" , "supra" , "gallardo" ]
shubh_fav = "camaro" or "supra" or "gallardo"  
for car in list:
    if car == shubh_fav:
     print(True)
    else:
     print(False)

     # creating an empty list
# lst = []
  
# number of elements as input
# n = int(input("Enter number of elements : "))
  
# iterating till the range
# for i in range(0, n):
    # ele = int(input())
    # adding the element
    # lst.append(ele)  
  
# print(lst)

# requeste_topp = ["mushrroms" , "cheese" , "mayoni"]

# for top in requeste_topp:
   
# print("adding" ,top)
#  if top == "cheese":
    # print("this tooping is  not avaialbe")
#  else:
    # print("adding" , top)

# checking a list is empty
# list = ["shubh"]
list = []
if list:
   for i in list:
      print(list)
else:
   print("yoou dont want anything")


requested_list = ["maggie" , "chai" , "biryani"]
for request_demand in requested_list:
   if request_demand == "biryani":
      print(f"soory {request_demand} is not  available") 
   else:
      print(f"Order Placed\n{request_demand}")


available_options = ["Success" , "Money" , "Fear" , "Aniexty"]
chhose_options = ["Success" , "consistency"]
for options in chhose_options:

   if options in available_options:
      print("ready your journey")

   else:
      print("this option is not available")

