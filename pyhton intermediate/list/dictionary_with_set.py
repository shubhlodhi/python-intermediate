languages = {"shubh" : "Pyhton",
             "mathew": "C",
             "cizar":"Python"
             }

# for fav in sorted(languages.values()):
for fav in set(languages.values()):
    print(f"some languages are {fav.title()}")
    if fav == "C":
        print(f"It's time to  leave this {fav.title()} language")
