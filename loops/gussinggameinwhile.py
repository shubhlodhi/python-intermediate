import random 
n = 20
guessed = int(n * random.random() )+1
print(guessed)
guess = int(input("enter first number"))
print(guess)
while guess != guessed:
    guess = int(input("new number"))

    if guessed>0:
        if guess> guessed:
          print("number is too large")

        elif guess<guessed:
          print("your number is too smaall")

    else:
        print("your are giving up")
        break
else:
      print("congrtas ,. whooo")