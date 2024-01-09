# pythogorean number
# pyhongorean number - a^2 + b^2 = c^2 
# example - 3^2, 4^2  , 5^2 are equal 
# 9 + 16 = 25

from math import sqrt
n = int(input("maximal number"))
for i in range(1,n+1):
    for j in range(i,n):
        # print(i,j)
        sw = i**2 + j**2
        c  = int(sqrt(sw))
        if (sw - c**2) == 0:
            print(i,j,c)