employee = {"shubh" : ["Python" , "Flask"],
            "Erin" : ["C" , "R"],
            "Mathew" :["C" , "PHP"]}

for i , j in employee.items():
    print(f"{i.title() } favirate languages are:")
    for k in j:
      print(k)



    #    a dictinary in a dictinary:

users = {"Shubh":{"Batch_number" : "25B",
                 "Work":"Coder" },
        "Erin": {"Batch_number": "23B",
                 "Work":"Status Updater"}}
                #  items() func is used to get the both values and keys pairs:
for i , j in users.items():
   print(i)
#    work = j["Batch_number"]  
   work = j.values()
   kk = j["Work"]
   print(work , kk)
#    for k in j.values() :
    # print(k)
#    for l in k :
    #   print(l)