from art import *

tprint("Tresure  Island")

print("find the tresure")

first_choice = input("left or right: ").lower()

if first_choice != "left":
    print("You falled in a hole , Game Over")
else:
    second_choice = input("swim or wait: ").lower()
    if second_choice != "wait":
        print("Attacked by a trout , Game Over")
    else:
        third_choice = input("Which door ? red , blue or yellow : ").lower()
        if third_choice == "blue":
            print("Eaten by beasts. Game Over")
        elif third_choice == "red":
            print("Burned by fire.Game Over")
        else:
            print("You found a tresure")
