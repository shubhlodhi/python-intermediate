# d = 5 
# k = 2*d-2
# d = 5
# for i in range(d,-1,-1):
    # print(i)
    # for j in range(k,-1,-1):
    #  print(end=" ")
    # k = k+1
    # for j in range(i+1):
    #    print("* " ,end="")

    # print("\r")

    # right strat pattern:

# d = 1
# for i in range(0,d):
#     for j in range(0,i+1):
#        print("* " , end="")
#     print("\r")
# for i in range(d,-1,-1):
# #     for j in range(0,i+1):
# #           print("* " , end="")
# #     print("\r")

#     # left start pattern:

# # d = 4
# # k  = 2*d-2
# # for i in range(d-1):
#     # for j in range(0,k):
#     #  print(i)
#     #  print(end="8")
#     # k = k -2

#     # for j in range(0,i+1):
#     #   print("* " , end="")
#     # print("\r")

# # k = k-1
#     # print(k)
# # print(k)
# # for i in range(d-1 , -1,-1):
#     # print(i)
#     # for j in range(k ,-1,-1):
#         # print(end="8")
#     # k = k+2    
#     # for j in range(0,i+1):
#         # print("* " , end="")
#     # print("\r")

# # Hour class pattern:
# d = 5
# # k = 2*d
# # for i in range ( d , -1 , -1):
#     # for j in range( 0 , k ):
#     #    print(end=" ")
#     # k = k+1
#     # for j in range(0 ,i+1):
#     #    print(end="* " )
#     # print("\r")
# # l = 2*d+5
# # for i in range(0,d+1):
# #    for j in range(0 ,l):
#     #  print(end=" ")
# #    l= l-1
# #    for j in range(0, i+1):
#     #   print("* " , end="")
# #    print("\r")  
# # half pyramid  / right pattern:
# # for i in range(0 , d):
#     # for j in range( 0 , i+1):
#         # print(end="* ")
#     # print("\r")
#     # print("\n")
# # left traingle pattern:
# k = 2*d-2
# for i in range( d ):

#     for j in range(0 ,k):
#         print(end="8")
#     # print("\r")
#     k = k-2 
#     for j in range(0 , i+1):
#         print(end="* ")
#         # k= k-1
#     print("\r")

#  diamond pattern :
d = 10
k = 2*d-2
for i in range(0 , d):
    for j in range(0 , k):
        print(end=" ")
    k = k-1
    for j in range(0 , i+1):
        print("* " , end="")
    print("\r")
for i in range(d , -1 ,-1):
    for j in range(k):
        print(end="9")
    k = k+1
    for j in range( 0 ,i+1):
        print("* " , end="")
    print("\r")

# diamond staer pattern:
for i in range(5):
    for j in range(5):
        if i +j == 2 or i-j ==2 or i+j == 6 or j-i==2:
            # print(i,j)
            print("*",  end="")
        else:
            print(end=" ")
    print()
    





     


       



