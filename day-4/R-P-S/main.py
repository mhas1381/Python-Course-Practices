from my_art import myart_list
from art import *
from random import randint
tprint("Welcome to Rock Paper Scissors")

user_choice = int(input("0 for Rock , 1 for Paper and 2 for Scissors:\n"))

computer_choice = randint(0 , 2)


print(myart_list[user_choice])
print(myart_list[computer_choice])

winning_cases = [(0,2) , (1 , 0) , (2 , 1)]

if user_choice == computer_choice:
    print("No Winner , Try Again")
elif (user_choice , computer_choice) in winning_cases:
    print("You Win")
else:
    print("You lost")