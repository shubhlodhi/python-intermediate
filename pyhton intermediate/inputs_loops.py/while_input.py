number = 0
while number<5:
    number += 1
    print(int(input(number)))

# prompt = "Please enter your details"
# prompt += "\nyour name is "
# # prompt += "\n Enter Quit to Exit"

# # message = " "
# # while message != "Quit":
# #     message = input(prompt)
# #     # print(message)
# #     if message != "Quit":
# #         print(message)


# # using a flag:
# # example - in a game ,several different events can end the game , like if time of player is out tgen it willl game over , so here we create a program here value is true
# #  if it is not true then it simply quit the game or game is over so we define the one variable which defines the entire program is in a active state or not.
# prompts = "\n tell me something and i will reapet it bak"
# prompts += "\n enter 'quit' to end the program"
# active = True # active indicate the flag:
# while active: # here its check only the whether the state is true : so as long as active variable is true the loop will continue
#     message = input(prompts)

#     if message == "Quit":
#         active = False
#     else:
#         print(message)

# # use break statement:
# po = "\n pease enter the name of city:"
# po += "\n enter 'Quit' to exit"
# while True:
#     city = input(po)

#     if city == "Quit":
#         break
#     else:
#         print(city)
# add continue statement in while loop:
show = "it's check the value is even or odd and print only odd value:"
show = "enter your number"

continuu = 0
while continuu <10:
    continuu+=1
    if continuu %2 ==0:
        continue
    else:
        print(continuu)
