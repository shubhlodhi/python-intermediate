# import pandas as pd
# hash table is a type of data structres that maps to its value pairs


# fisrt we want to know how to create a dictinary
my_dict = {"shubh": 123}
print(type(my_dict))
print(my_dict)
# dict() function:
new_dict = dict()
print(new_dict)
print(type(new_dict))
new_dict = dict(shubh = 123 , lodhi=  234)
print(new_dict)
# nested dictinaries: are type of dictinary that lie within other dictionary
s = {"employee":{"lodhi":{"id":"00","occupatin":"coder"},"shubh":{"id":"001" , "oocupation":"1000"  }}}
# print(s)
f  ={"name":{"shubh":{"work":"23s" , "salary":"20k"},
"khushi":{"work":"23s" , "salary":"23k"}

}
}
# print(f)

# performing operation in hash table:
# accessing items
# updating items
#  deleting entries

# Accesing items:
print(new_dict.keys())
print(new_dict.values())
print(new_dict.get("shubh"))

for i in new_dict.values():
    print(i)
for i in new_dict.keys():
    print(i)
# here we accessing the items of dict
for i,y in new_dict.items():
    print(i,y)

# updating the dictionary:

new_dict["shubh"] = "001"
# here we add the new key-value pair in new_dict
new_dict["khushi"] = "234"
print(new_dict)
# shubh = {"sneha":123}
# f = new_dict.update(shubh)
# print(f)
# deleting function in dict:
new_dict.pop("lodhi")
print(new_dict)
new_dict.popitem()
# it pop the last items in dictionary
print(new_dict)
del new_dict["shubh"]
# delete function delete with the help of key in dictionary
print(new_dict)
# cinvert dictinary into data frames:
# data frame is  a 2-d(2 dimensional) data sturcture that consists of columns of various types.it is very similar to a python dictinary
# and you can even convert a dictionary into  a pandas data frame 

# df = pd.dataframe(f["employee"])
# print(df)



