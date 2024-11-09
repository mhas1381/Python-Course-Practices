from art import logo
from os import system
print(logo)

is_continue = True
bids={}

def find_highest_bidder(bid_record):
    highest_bid = 0
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        print(f"The winner is {winner} with {highest_bid}$")


while is_continue:
    name = input("What is your name:\n")
    bid_amout = int(input("What is your bid is $:\n"))
    bids[name] = bid_amout
    q = input("Are there any bidders:Y/N\n").lower()
    system("cls")
    if q == "n":
        find_highest_bidder(bids)
        is_continue = False