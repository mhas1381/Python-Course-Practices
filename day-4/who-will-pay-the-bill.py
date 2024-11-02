from random import randint , choice

names_string = input("Enter name sepreted by , :\n")
names = names_string.split(",")
rand = randint(0,len(names)-1)
print(f"{names[rand]} is going to pay the bill")
print(f"{choice(names)} is going to pay the bill")