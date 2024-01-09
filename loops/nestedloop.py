# a program in python that effectively simulates a bank atm

# task 1 - enter pin
#  task 2 - option: check balance , make a withdrawl , pay in , return card
# i have only 3 chances for pin
import random
print("welcome to my bank")
chances = 3
restart = (str(random.random()))
balance = 20000
while chances >= 0:
    pin = int(input("enter your pin "))
if pin == (1234):
    print("you enter coorect pin")
    while restart not in ("n", "not", "N"):
        print(restart)
        print("press 1 for chack your balance")
        print("press 2 for make a withdrwal")
        option = int(input("choose your option"))
        if option == 1:
            print("your balance is ", balance)
            restartf = input("what would you like to go back")
            if restartf == restart:
                print("thank you")
                break
        elif option == 2:
            print("withrwal amount")
            # option2 ="Y"
            withdrwal = float(input("enter your withdrawl amount"))
            if withdrwal in [10, 20, 30, 40]:
                balance = balance - withdrwal
                print("our cirrent balance", balance)
                # restart = "y"
                restartn = input("go bak or not")
                if restartn == restart:
                    print("thank you")
                    break
            elif withdrwal != [10, 20, 30, 40]:
                print("invalid amount")
                restart = "y"
            elif withdrwal == 1:
                print("you have low balance")
        elif option == 3:
            print("your paid amount ")
            paid = int(input("your amoount is "))
            print(paid)
            balance = balance + paid
            print("cureent amount is", balance)
            restartg = input("would you like to go back")
            if restartg == restart:
                print("thank you")
                break

elif pin != 1234:
        print("pin is inscorrect")

        chances = chances - 1
        print("please enter right pin")
        print(f"chances are left now{chances}")
        if chances == 0:
          print("no more tries")
          
    #  else:
    #       print("please enter right pin")
    #       print(f"you have now only {chances} left")
