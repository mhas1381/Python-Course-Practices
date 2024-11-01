print("Welcome to pizza delivery app")
size = input("What size pizza do you want ? S,M or L: ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "s":
    bill = 15
elif size == "m":
    bill = 20
elif size == "l":
    bill = 25

if size == "s" and add_pepperoni == "y":
    bill += 2
elif add_pepperoni == "y":
    bill += 3
if extra_cheese == "y":
    bill +=1

print(f"Your final bill is {bill}")
