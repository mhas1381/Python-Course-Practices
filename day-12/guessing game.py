from random import randint

numbers = []
chances = 0
is_game_going = True

random_number = randint(1 , 100)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose difficulty.type 'easy' or 'hard': ")
if difficulty == "easy":
    chances = 10
else:
    chances = 5

while is_game_going:
    print(f"You have {chances} attempts remaining to guess the number.")
    user_guess = int(input("Guess a number: "))
    if chances == 0:
        is_game_going = False
    if user_guess == random_number:
        print("You Guess right")
        is_game_going = False
    elif user_guess > random_number:
        print("Too high")
        chances -= 1
    else:
        print("Too low")
        chances -= 1
