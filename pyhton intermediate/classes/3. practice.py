from practice import restaurant, user


class icecream( restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavoures = []

    # def show_user(self):
    #     print(f"name:{self.name}\n type:{self.type}\n")

    def add_flavours(self , flavor):
        self.flavoures.append(flavor)

    def show(self):
        print(f"show the flvaoures: {self.flavoures}")


person = icecream("crud" , "Non-Veg")
print(person.describe_restaurant())
# print(person.show_user())
print(person.add_flavours("Vanilla"))
print(person.add_flavours("Chocolate"))
print(person.show())


class admin(user):
    def __init__(self, name, E_mail, Username):
        super().__init__(name, E_mail, Username)
        self.privelge = ["edit the post" , "delete the post" ,"update the post"]

    def show(self):
        print(f"the privelages are {self.privelge}")



    def make_Privelges(self , new_priv):
        self.privelge.append(new_priv)

person = admin("shubh" , "shubh.singh9411@gmail.com" , "SSlrp")
print(person.describe_user())
print(person.show())
print(person.make_Privelges("edit the vlog"))
print(person.show())

    