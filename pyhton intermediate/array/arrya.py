# an array is basically  a data structures which can hold more than one value at a time. it is a collection or orederd series of elements of the same things
# array in python can be created after importing the array 
# without alias  = import array
# with alias = import array as arr
# using*  = from array import *
# import array
# arr = array.array("i",[1,2,3,43,5])
# print(arr) 

# here first array is indicates the array module and second is the array constructor
# i is indicates that only integer value is stored in this array or indicates the data structure

import array as arr
arry = arr.array("i" , [1,2,3,4,5])
print(arry)

# from array import *
# arrt = array("i" , [1,2,3,4])
# print(arrt)

#  Accesing the array elements
# acces elemnts using index values
# indexing atarts at 0 and not from 1 . hence teh index number is always 1 less than the length of the array
#  also used negative index value ex: right to left

# print(arrt[2])


# basic array operations:
# finding the length of an array
# adding/changing element of an array
# array conactination
# removing /deleting elements from an array
# slicing of an array
# looping through an array

# 1: length of an array using( len() ) function
# it returns the integer value

arrf = arr.array("i" , [1,2,3,4,5])
print(len(arrf))

# adding elements to an array
# 1:append()
# 2:extend()
# 3:insert()

arrf.append(1)
print(arrf)
arrf.extend([11,2,3])
print(arrf)
arrf.insert(2,3) 
# here 2 indicates the index numnber the value which stores 3.

print(arrf)
#  removing elements of an array :
#  pop()
# remove()
print(arrf.pop())
print(arrf.pop(7))
print(arrf)
# it remove the last value and index value 
print(arrf.remove(5))
# it remove the value which are specify in the paraemeter

print(arrf)
#  array conactinatioon
# where we add the two same arrya
a = arr.array("i" , [34,45,56,12,12,12,12,12,1,21,2])
# c = arr.array("i")
# c = "adding two value " , arrf+a
# print(c) 
# slicing an array:
# print(a[0:3])
# print(a[::-1])
# it reverses the array
#  use in for and while:
# for i in (a):

#     print(i)
# for i in a[1:2]:
#     print(i)
emp = 0
while (emp<a[6]):
    print(a[emp]) 
    emp  +=1
temp = 0
while(temp<len(a)):
    print((a[temp]))
    # i = 0
    # print(i)
    # i+=1
    temp+=1
