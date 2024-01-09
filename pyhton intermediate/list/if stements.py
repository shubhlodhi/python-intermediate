# requested_toppinng = "mushrooms" , "extra cheese"
requested_toppinngs = list(input("please enter your choice" ))

order = "shubh"
if "mushrooms" in requested_toppinngs:
    print(f"add mushrooms in order of{order.title()}")
if "extra cheese" in requested_toppinngs:
    print(f"add exrta cheese in order of {order.title()}")
else:
    print(f"please dispatch the order of " , order.title())

