from random import choice
from art import tprint
from hangman_art import hangman_stages
import os, time
tprint("HangMan")
word_list = ["ardvark", "baboon", "camel"]
random_word = choice(word_list)
print(f"the choosen word is {random_word}")
end_of_game = True
blank_list = []
lives = 6
for _ in random_word:
    blank_list.append("_")
while end_of_game:
    letter = input("Guess a word:\n").lower()
    os.system("cls")
    time.sleep(0.1)
    for position in range(len(random_word)):
        if letter == random_word[position]:
            blank_list[position] = letter
    if letter not in random_word:
        lives -=1
        print(hangman_stages[lives])
        print(f"Your remaining lives :{lives}")
        if lives == 0:
            end_of_game = False
            print("You lose")
    if list(random_word) == blank_list:
        end_of_game = False
        print("You have completed game.")

    print(" ".join(blank_list))

