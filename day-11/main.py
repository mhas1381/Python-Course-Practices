from random import choice
from os import system
user_choice = input("Do you want to play blackjack?[Y/N]\n").lower()
is_game_over = False
is_continue = False

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(cards_list):
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    if sum(cards_list) > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose , opponent has Blackjack"
    elif user_score == 0:
        return "You win with a blckjack"
    elif user_score > 21:
        return "You went over , You lose"
    elif computer_score > 21:
        return "Opponent went over , You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards is : {user_cards} and score is : {user_score}")
        print(f"Computer first card is {computer_cards[0]}")
        if user_score == 0 or user_score > 21 or computer_score == 0:
            is_game_over = True
        else:
            draw_another_card = input("Do you want draw another card?[Y/N]").lower()
            if draw_another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your cards : {user_cards} and final score: {user_score}")
    print(f"Computer cards : {computer_cards} and final score: {computer_score}")
    print(compare(user_score , computer_score))

user_continue = input("Do you want to continue:[Y/N]").lower()
if user_choice == 'y':
    system("cls")
    play_game()
