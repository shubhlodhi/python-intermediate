from random import choice
import random
class die:
    def __init__(self , sides=6):
        self.sides = sides

    def roll(self):
        # first we import the random then we define in the randit method from 1 to number of sides. and store in the result 
       
        result = random.randint(1, self.sides)
        print(f"The dice rolled: {result}")
        return result

h = die()
for i in range(10):
 (h.roll())


class lottery:
   def __init__(self ):
      self.list = [1,2,3,4,5,6,7,8,9,10, "s" , "d" , "f"]
    #   self.sample = sample

   def lot(self):
      result = random.sample(self.list , 4)
      
      return result
   def check(self  ,result ):
    #    for i in result():
         if result in ["s" , "d" , "f" , 1]:
            print(result)
            return True
         else:
          return False
      
   
g = lottery()
print(g.lot())
p = (g.lot())
print(g.check(p))
if g.check(p):
    print("Congratulations! You have won a prize!")
else:
    print("Sorry, this ticket does not win a prize.")